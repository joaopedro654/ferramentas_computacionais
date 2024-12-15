import cv2
import numpy as np

# Carregar a imagem de satélite
filename = "brasil_coverage_2022.tif" 
image = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)

# 1. Quantidade total de pixels
total_pixels = image.size

# 2. Quantidade de pixels sem dados (código 0)
no_data_pixels = np.sum(image == 0)

# 3. Quantidade de pixels correspondente ao plantio de Soja (código 39)
soja_pixels = np.sum(image == 39)

# 4. Quantidade de pixels correspondente à pastagem (código 15)
pastagem_pixels = np.sum(image == 15)

# Remover os pixels sem dados para o cálculo de área utilizável
valid_pixels = total_pixels - no_data_pixels

# Área total do Brasil em hectares (dados do IBGE)
area_brasil_hectares = 851576700  # Valor aproximado em hectares

# Percentuais de soja e pastagem
soja_percent = (soja_pixels / valid_pixels) * 100
pastagem_percent = (pastagem_pixels / valid_pixels) * 100

# Cálculo da área correspondente em hectares
soja_area_hectares = (soja_percent / 100) * area_brasil_hectares
pastagem_area_hectares = (pastagem_percent / 100) * area_brasil_hectares

# Resultados
print(f"Total de pixels na imagem: {total_pixels}")
print(f"Pixels sem dados (código 0): {no_data_pixels}")
print(f"Pixels de plantio de Soja (código 39): {soja_pixels}")
print(f"Pixels de pastagem (código 15): {pastagem_pixels}")
print(f"Área de plantio de soja: {soja_area_hectares:.2f} hectares ({soja_pixels} pixels)")
print(f"Área de cobertura de pastagem: {pastagem_area_hectares:.2f} hectares ({pastagem_pixels} pixels)")