from stages import model_lead
import repo

def add_lead():
    name = input("Digite o nome do lead: ")
    email = input("Digite o email do lead: ")
    company = input("Digite a empresa: ")
    stage = input("Digite o estagio de vendas : ")

    if not name or not email or "@" not in  email:
        print("Nome e/ou e-mail válido são obrigatórios")
        return



    #precisar chamar model para modelar os dados
    print(model_lead(name, email, company, stage))

    #depois de modelado...

    #vou precisar chamar repo.py para enviar os dados modelados para o banco de dados json
    repo.create_lead(model_lead(name, email, company, stage))

def list_leads():
    leads = repo.read_leads()

    if not leads:
        print("nenhum lead ainda")
        return

    print("\n# | Nome        | Empresa   | Email ")
    for i, lead in enumerate(leads):
        print(f"{i: 02d}| {lead['name']: <20} | {lead['company']: <20} | {lead['email']}1")

def search_leads():
   query = input("Buscar por ").strip().lower()
   if not query:
       print("Consulta vazia")
       return


   leads_finded = repo.read_leads_search(query)

   print("\n# | Nome        | Empresa   | Email ")
   for i, lead in enumerate(leads_finded):
       print(f"{i: 02d}| {lead['name']: <20} | {lead['company']: <20} | {lead['email']}1")

def export_leads():
    path_csv = repo.export_csv()


    if path_csv is None:
        print("nao foi possivel exportar os leads para CSV")
    else:
        print(f'CSV exportando para {path_csv}')


def main():
    while True:
        print("\nMini CRM - 1 aula -(adicionar/listar")
        print("[1] Adicionar lead")
        print("[2] Listar leads")
        print("[3] Buscar (nome/email/empresa)")
        print("[4] Exportar para CSV")
        print("[0] Sair do programa")

        opt = input("Digite uma opcao: ").strip()
        if opt == "1":
            add_lead()
        elif opt == "2":
           list_leads()
        elif opt == "3":
            search_leads()
        elif opt == "4":
            export_leads()
        elif opt == "0":
            print("Ate mais")
            break
        else:
            print("Opcao invalida")



if __name__ == "__main__":
    main()
