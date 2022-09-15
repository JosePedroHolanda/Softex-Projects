import pandas as pd

df = pd.read_csv("notas_alunos.csv")

media = (df["nota_1"]+df["nota_2"])/2
df["media"] = media

df.loc[df["faltas"] <= 5, "situacao"] = "APROVADO"
df.loc[df["faltas"] > 5, "situacao"] = "REPROVADO"
df.loc[df["media"] < 7, "situacao"] = "REPROVADO"

df.to_csv("alunos_situacao.csv")

print("O maior número faltas foram: {}".format(df["faltas"].max()))
print("A média geral das notas foi de {}".format(df["media"].median()))
print("A maior media foi de {}".format(df["media"].max()))
