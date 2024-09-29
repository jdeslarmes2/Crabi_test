import pandas as pd

# Cargar los archivos Excel
claim_df = pd.read_excel('C:/Users/javie/Documents/Javi/Personal/Crabi/data/claim.xlsx')
people_df = pd.read_excel('C:/Users/javie/Documents/Javi/Personal/Crabi/data/people.xlsx')
service_df = pd.read_excel('C:/Users/javie/Documents/Javi/Personal/Crabi/data/service.xlsx')
status_df = pd.read_excel('C:/Users/javie/Documents/Javi/Personal/Crabi/data/status.xlsx')

# Cruce 1: Claim y Status
final_claim = pd.merge(claim_df, 
                        status_df[['id', 'name', 'description']], 
                        left_on='type_status_id', right_on='id', how='left')

# Renombrar columnas
final_claim.rename(columns={'name': 'claim_name', 'description': 'claim_description'}, inplace=True)
# Eliminar columna duplicada
final_claim.drop(columns=['id_y'], inplace=True)

# Guardar resultado final_claim
final_claim.to_excel('C:/Users/javie/Documents/Javi/Personal/Crabi/data/final_claim.xlsx', index=False)

# Cruce 2: People y Status
final_people = pd.merge(people_df, 
                         status_df[['id', 'name', 'description']], 
                         left_on='type_status_id', right_on='id', how='left')

# Renombrar columnas
final_people.rename(columns={'name': 'people_name', 'description': 'people_description'}, inplace=True)
# Eliminar columna duplicada
final_people.drop(columns=['id_y'], inplace=True)

# Guardar resultado final_people
final_people.to_excel('C:/Users/javie/Documents/Javi/Personal/Crabi/data/final_people.xlsx', index=False)

# Cruce 3: Service y Status para service_name y service_description
status_df_renamed = status_df.rename(columns={'description': 'service_description'})
final_service = pd.merge(service_df, 
                          status_df_renamed[['id', 'name', 'service_description']], 
                          left_on='type_status_id', right_on='id', how='left')

# Renombrar columnas
final_service.rename(columns={'name': 'service_name'}, inplace=True)

# Agregar coverage_name y coverage_description
status_df_renamed_coverage = status_df.rename(columns={'description': 'coverage_description'})
final_service = pd.merge(final_service, 
                          status_df_renamed_coverage[['id', 'name', 'coverage_description']], 
                          left_on='coverage_id', right_on='id', how='left')

# Renombrar columnas
final_service.rename(columns={'name': 'coverage_name'}, inplace=True)

# Eliminar la columna 'id' generada durante el último merge
final_service.drop(columns=[col for col in final_service.columns if col.startswith('id') and col != 'id_x'], inplace=True)

# Guardar resultado final_service
final_service.to_excel('C:/Users/javie/Documents/Javi/Personal/Crabi/data/final_service.xlsx', index=False)

print("Archivos finales generados: final_claim.xlsx, final_people.xlsx, final_service.xlsx")