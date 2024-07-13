"""
Extraccion de los nombres de las imagenes
"""

class ImgData:
    """
    Esta clase devuelve la data de las imagenes
    """

    def pasar_imagenes(self, img):
        """ 
        Devuelve el nombre de la imagen con su extencion  
        
        Parameters: 
        song (str): el path 

        Returns:
        str: el nombre y extencion de la imagen
        """
        print(f"Leyendo los datos de {img}")