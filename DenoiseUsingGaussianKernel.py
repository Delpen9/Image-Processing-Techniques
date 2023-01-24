import cv2

def gaussian_denoise(
  image : np.ndarray,
  kernel_size : int = 3,
  standard_deviation : int = 2
):
  '''
  gaussian_denoise()
  '''
  kernel = cv2.getGaussianKernel(kernel_size, standard_deviation)
  denoised_image = cv2.sepFilter2D(image, -1, kernel, kernel)
  return denoised_image
