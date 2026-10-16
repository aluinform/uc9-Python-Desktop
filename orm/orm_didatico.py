from sqlalchemy import String, create_engine, select
from sqlalchemy.orm import DeclarativeBase, Mapped, Session, mapped_column

class Base(DeclarativeBase):
    pass

class Aluno(Base):
    __tablename__ = "alunos"

    id: Mapped[int] = mapped_column(primary_key=True)
    nome: Mapped[str] = mapped_column(String(100))
    email: Mapped[str] = mapped_column(String(150), unique=True, index=True)

engine = create_engine("sqlite:///escola.db")

Base.metadata.create_all(engine)

with Session(engine) as session:
    
    # Inserindo um novo aluno
    novo_aluno = Aluno(nome="Eric Azevedo", email="eric@gmail.com")
    session.add(novo_aluno)
    session.commit()

# READ
consulta = select(Aluno).where(
    Aluno.email == "eric@gmail.com"
)
aluno_encontrado = session.scalars(consulta).first()
print(f"Consulta: ", aluno_encontrado.nome)

# UPDATE
aluno_encontrado.nome = "Eric da Silva"
session.commit()

# READ UPDATE
print("Nome atualizado: ", aluno_encontrado.nome)

# DELETE
session.delete(aluno_encontrado)
session.commit()

print("Operações concluídas!")