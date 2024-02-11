
import streamlit as st 
st.title("PRODUTOS")

opcao = st.sidebar.selectbox("Selecione uma ação",("Adicionar Produto", "Listar Produtos"))

produtos = [
    {"id": 1, "nome": "MI BAND 7 PRO", "preco": 379.00},
    {"id": 2, "nome": "Mouse GAMER REDRAGON", "preco": 79.00},
    {"id": 3, "nome": "Mousepad REDRAGON", "preco": 120.00},
    {"id": 4, "nome": "SSD KINGSTON 1TB", "preco": 800.00},
    {"id": 5, "nome": "Monitor GAMER 120HZ", "preco": 2519.00},
]

def listar_produtos():
    st.subheader("Lista de Produtos")
    for produto in produtos:
        st.write(f"ID: {produto["id"]}, Nome: {produto["nome"]}, preco: {produto["preco"]}")
        
        
def adicionar_produtos():
    st.subheader("Adicionar Produto")
    nome = st.text_input("Nome do Produto")
    preco = st.number_input("Preço do produto")
    if st.button("Adicionar"):
        novo_produto ={"id": len(produtos) +1, "nome": nome, "preco": preco}
        produtos.append(novo_produto)
        st.success("Produto adicionado com sucesso!")
        
if opcao == "Adicionar Produto":
    adicionar_produtos()
elif opcao == "Listar Produtos":
    listar_produtos()