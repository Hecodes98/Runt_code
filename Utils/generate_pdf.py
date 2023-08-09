import os
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet

# Ruta de la carpeta que contiene las imágenes
SCHEDULING_PATH = '../evidences/scheduling'
ORGANIZATIONS_PATH = '../evidences/test_organizations'
NEW_ROOM_PATH = '../evidences/new_room_creation'
ASSISTANT_REGISTRATION_PATH = '../evidences/test_assistant_registration'
CONSULT_INFORMATION_PATH = '../evidences/test_consult_information_infractions'
paths = [SCHEDULING_PATH, ORGANIZATIONS_PATH, NEW_ROOM_PATH, ASSISTANT_REGISTRATION_PATH, CONSULT_INFORMATION_PATH]
imagenes = list()
# Función para recorrer directorios de manera recursiva
def recorrer_directorios(ruta):
    imagenes = []
    for carpeta_actual, subcarpetas, archivos in os.walk(ruta):
        for archivo in archivos:
            if archivo.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
                ruta_imagen = os.path.join(carpeta_actual, archivo)
                imagenes.append(ruta_imagen)
    return imagenes

# Obtener la lista de rutas de imágenes en todas las subcarpetas
for path in paths:
    imagenes += recorrer_directorios(path)

# Crear un documento PDF
doc = SimpleDocTemplate("lista_imagenes_subcarpetas.pdf", pagesize=letter)

# Definir estilos para el documento
styles = getSampleStyleSheet()

# Lista para almacenar los elementos que se agregarán al PDF
contenido = []

# Agregar título
titulo = Paragraph("Evidencias capturadas", styles['Title'])
description = Paragraph("El ID de la evidencias se encuentra al pie de la evidencia", styles['Normal'])
contenido.append(titulo)
contenido.append(Spacer(1, 12))

# Agregar las imágenes y sus nombres de archivo
for imagen in imagenes:
    img = Image(imagen, width=400, height=400)
    contenido.append(img)
    contenido.append(Spacer(1, 12))
    nombre_archivo = Paragraph(os.path.basename(imagen), styles['Normal'])
    contenido.append(nombre_archivo)
    contenido.append(Spacer(1, 12))

# Construir el documento PDF
doc.build(contenido)

print("Documento PDF generado exitosamente.")
