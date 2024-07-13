import numpy as np
from numpy.linalg import norm, eig
import sys


class HaloOrientation():

    @staticmethod
    def rotate(v, phi, theta, psi):
        """Rotate vectors in three dimensions

        Arguments:
            v: vector or set of vectors with dimension (n, 3), where n is the
                number of vectors
            theta: angle between 0 and 2pi
            phi: angle between 0 and pi
            psi: angle between 0 and pi

        Returns:
            Rotated vector or set of vectors with dimension (n, 3), where n is the
            number of vectors
        """

        v_new = np.zeros(np.shape(v))

        Rx = np.matrix(
            [
                [1, 0, 0],
                [0, np.cos(phi), -np.sin(phi)],
                [0, np.sin(phi), np.cos(phi)],
            ]
        )

        Ry = np.matrix(
            [
                [np.cos(theta), 0, np.sin(theta)],
                [0, 1, 0],
                [-np.sin(theta), 0, np.cos(theta)],
            ]
        )

        Rz = np.matrix(
            [
                [np.cos(psi), -np.sin(psi), 0],
                [np.sin(psi), np.cos(psi), 0],
                [0, 0, 1],
            ]
        )

        R = Rx * Ry * Rz
        v_new += R * v

        return v_new

    @staticmethod
    def transform(v1, v2):
        """transform to different coordinate system

        Arguments:
            v1: vector or set of vectors with dimension (3, n), where n is the
                number of vectors
            v2: principal axis of desired coordinate system 

        Returns:
            Vector or set of vectors in new coordinate system with dimension
            (3, n), where n is the number of vectors
        """

        v_new = np.zeros(np.shape(v1))

        # loop over each of thse 3 coordinates
        for i in range(3):
            v_new[i] += v1[0] * v2[i, 0] + v1[1] * v2[i, 1] + v1[2] * v2[i, 2]

        return v_new

    @staticmethod
    def uniform_random_rotation_simple(v):
        """Do uniform random 3D rotation using Euler angles

        Args:
            v (array): (3, n) coordinate vector where n is number of vectors

        Returns:
            v_new (array): rotated vectors
            phi (float): rotation angle
            theta (float): rotation angle
            psi (float): rotation angle
        """

        phi = 2*np.arccos(2*np.random.random()-1)
        theta = np.arccos(2*np.random.random()-1)
        psi = np.arccos(2*np.random.random()-1)

        v_new = HaloOrientation.rotate(v, phi, theta, psi).T

        return v_new, phi, theta, psi

    @staticmethod
    def generate_random_z_axis_rotation():
        """Generate random rotation matrix about the z axis."""

        R = np.eye(3)
        x1 = np.random.rand()
        R[0, 0] = R[1, 1] = np.cos(2 * np.pi * x1)
        R[0, 1] = -np.sin(2 * np.pi * x1)
        R[1, 0] = np.sin(2 * np.pi * x1)

        return R

    @staticmethod
    def uniform_random_rotation(x):
        """Apply a random rotation in 3D, with a distribution uniform over the
        sphere.

        Arguments:
            x: vector or set of vectors with dimension (n, 3), where n is the
                number of vectors

        Returns:
            Array of shape (n, 3) containing the randomly rotated vectors of x,
            about the mean coordinate of x.

        Algorithm taken from "Fast Random Rotation Matrices" (James Avro, 1992):
        https://doi.org/10.1016/B978-0-08-050755-2.50034-8
        """

        # There are two random variables in [0, 1) here (naming is same as paper)
        x2 = 2 * np.pi * np.random.rand()
        x3 = np.random.rand()

        # Rotation of all points around x axis using matrix
        R = HaloOrientation.generate_random_z_axis_rotation()
        v = np.array([np.cos(x2) * np.sqrt(x3), np.sin(x2)
                     * np.sqrt(x3), np.sqrt(1 - x3)])
        H = np.eye(3) - (2 * np.outer(v, v))
        M = -(H @ R)
        x = x.reshape((-1, 3))
        mean_coord = np.mean(x, axis=0)

        return ((x - mean_coord) @ M) + mean_coord @ M

    @staticmethod
    def get_eigs(I, rvir):
        """Get eigenvalues and eigenvectors of halo inertia tensor

        Arguments:
            I (array): host halo inertia tensor
            rvir (array): halo virial radius

        Returns:
            array: eigenvalues
            array: eigenvectors
        """
        # return eigenvectors and eigenvalues
        w, v = eig(I)

        # sort in descending order
        odr = np.argsort(-1.0 * w)

        # sqrt of e values = A,B,C where A is the major axis
        w = np.sqrt(w[odr])
        v = v.T[odr]

        # rescale so major axis = radius of original host
        ratio = rvir / w[0]
        w[0] = w[0] * ratio  # this one is 'A'
        w[1] = w[1] * ratio  # B
        w[2] = w[2] * ratio  # C

        return w, v

    @staticmethod
    def get_random_axes_and_angles(princip_axes):
        """Define set of randomly oriented axes by rotating principal axes
            and calculate azimuthal angle between new axis and major axis

        Args:
            princip_axes (array): Principal axes 3x3 array
                princip_axes.T[0] corresponds to major axis
                princip_axes[0] corresponds to i-th component of vectors

        Returns:
            new_axes (2d array): set of 3 orthogonal vectors
                shape is 3x3
                new_axes[0] corresponds to first vector
                new_axes.T[0] corresponds to i-th component of vectors

            angle (float): azimuthal angle between long axes of both axes sets
            phi (float): first Euler angle
            theta (float): second Euler angle
            psi (float): third Euler angle
        """

        # returns angles in radians
        new_axes, phi, theta, psi = HaloOrientation.uniform_random_rotation_simple(
            princip_axes)

        angle = np.dot(new_axes[0], princip_axes.T[0]) / (
            np.linalg.norm(new_axes[0]) * np.linalg.norm(princip_axes.T[0])
        )  # -> cosine of the angle

        return new_axes, angle, phi, theta, psi

    @staticmethod
    def check_ortho(e_vect):
        """Check if eigenvectors inertia tensor are orthogonal

        Arguments:
            e_vect (array): 3x3 array of inertia tensor eigenvectors
                For consistency with rest of methods:
                    e_vect.T[0] corresponds to major axis
                    e_vect[0] corresponds to i-th component of vectors


        """

        # define a diagonal matrix of ones
        a = np.zeros((3, 3))
        np.fill_diagonal(a, 1.)

        # take dot product of e_vect and e_vect.T
        # off diagonals are usually 1e-15 so round them to 0.
        m = np.abs(np.round(np.dot(e_vect, e_vect.T), 1))

        # check if all elements are equal to identity matrix
        if np.any(a != m):
            sys.exit(1)

    @staticmethod
    def get_axis_ratios(e_values):
        """Return axis ratios from array of eigenvalues

        Arguments:
            e_values (array): 3x1 array of inertia tensor eigenvalues

        Returns:
            s: ratio of shortest axis to longest axis
            q: ratio of intermediate axis to longest axis
        """
        a, b, c = e_values
        s = c/a
        q = b/a

        return s, q

    @staticmethod
    def get_perp_dist(v, pos):
        """ Return component of vector perpendicular to major axis
        and its angular separation from major axis

        Arguments:
            v: vector defining axis of interest (example: major axis)
            pos: position (x,y,z) vector or set of vectors with dimension (n, 3), 
                where n is the number of vectors

        Returns:
            perp: component perpendicular to axis of interest
            angle: angular separation between axis of interest and position vector
        """

        v2 = np.repeat(v, len(pos)).reshape(3, len(pos)).T

        # calculate angular separation in radians between position vector and major axis
        angle = np.arccos(
            abs((pos*v2).sum(axis=1)/(norm(pos, axis=1)*norm(v))))

        # dot product to find magnitude of component
        # of position vectors parallel to major axis
        para1 = (pos * v2 / norm(v)).sum(axis=1)

        # normalized major axis vector
        para2 = (v / norm(v)).T

        # parallel vector (magnitude and direction)
        para = np.array((para2[0] * para1, para2[1] * para1, para2[2] * para1))

        # perpendicular component
        perp = pos - para.T

        return perp, angle

    @staticmethod
    def cut_data(p, p1, s, q, rvir):
        """ Remove particles that fall outside ellipsoid defined
        by new inertia tensor

        Arguments:
            p: (array) particle coordinates in original coordinate system with shape = (3, n)
            p1: (array) particle coordinates in principal axes coordinate system with shape = (3, n)
            s: short axis to long axis ratio
            q: intermediate axis to long axis ratio
            rvir: virial radius or max value for eigenvalues

        Returns:
            new_p: (array) trimmed down particle coordinates in original coordinate system
            new_p1: (array) trimmed down particle coordinates in principal axes coordinate system
        """

        # calculate particle distances in new coord system
        d = p1[0]**2 + (p1[1]/q)**2 + (p1[2]/s)**2
        cut = d < 0.00017**2
        d[cut] = 0.00017**2  # particle distances should not be below force resolution

        # determine which are within the bounds
        cut = d <= (rvir**2)
        # trimmed down in principal axes coordinate system
        new_p1 = p1.T[cut].T
        new_p = p.T[cut].T  # in orig coordinate system

        return new_p, new_p1

    @staticmethod
    def get_inertia_tensor(p, s=1.0, q=1.0, p1=None, normalize=False):
        """ Calculate inertia tensor from particles
        (assuming equal mass particles)

        Arguments:
            p: position vector (x,y,z) for particle or set of particles
              with dimension (3, n), where n is the number of vectors
            s: (default: 1) axis ratio (short/long)
            q: (default: 1) axis ratio (mid/long)
            p1: (default: None) position vector (x,y,z) for particle or set
                of particles with dimension (3, n), where n is the number 
                of vectors in frame of principle axis
            normalize: (default: False) whether to normalize by particle distance
                from center

        Returns:
            I: (array) inertia tensor 
        """

        if normalize == True:
            r2 = (p1[0]**2 + (p1[1]/q)**2 + (p1[2]/s)**2)

        else:
            r2 = 1.0

        Ixx = np.sum((p[0]*p[0])/r2)
        Iyy = np.sum((p[1]*p[1])/r2)
        Izz = np.sum((p[2]*p[2])/r2)
        Ixy = np.sum((p[0]*p[1])/r2)
        Iyz = np.sum((p[1]*p[2])/r2)
        Ixz = np.sum((p[0]*p[2])/r2)
        Iyx = Ixy
        Izy = Iyz
        Izx = Ixz
        I = np.array(((Ixx, Ixy, Ixz), (Iyx, Iyy, Iyz), (Izx, Izy, Izz)))

        return I

    @staticmethod
    def fit_inertia_tensor(p, rvir):
        """ Iterative routine to find inertia tensor based on Zemp et. al. 2011

        Arguments:
            p: position vector (x,y,z) for particle or set of particles
              with dimension (3, n), where n is the number of vectors
            rvir: (float) virial radius of host halo

        Returns:
            I: (array) inertia tensor
        """

        s, q = 1., 1.
        I = HaloOrientation.get_inertia_tensor(p, s, q)
        tol = .001
        it = 0
        err = 1.

        while err > tol:
            s_old, q_old = s, q

            # get eigen vectors and values of inertia tensor
            w, v = HaloOrientation.get_eigs(I, rvir)

            # check if vectors are orthonormal
            HaloOrientation.check_ortho(v)

            # get new s and q
            s, q = HaloOrientation.get_axis_ratios(w)

            # rotate to frame of principle axis
            p1 = HaloOrientation.transform(p, v)

            # select which particles fall within new ellipsoid
            p, p1 = HaloOrientation.cut_data(p, p1, s, q, rvir)

            # recalculate inertia tensor
            I = HaloOrientation.get_inertia_tensor(p, s, q, p1, normalize=True)

            # compare err to tolerance
            err1 = abs(s_old-s)/s_old
            err2 = abs(q_old-q)/q_old
            err = max(err1, err2)

            it += 1

            if it > 9:
                return I

        return I
