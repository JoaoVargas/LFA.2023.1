import pyautogui
import time
 
def texto(): 
     for i in range(1,21):
          time.sleep(0.1)
          #pyautogui.hotkey("ctrl", "v"")
          pyautogui.write("BI{0}_Geral, ".format(i))
          #pyautogui.hotkey("ctrl", "v")
          #pyautogui.write(' ' + str(i) + "                 x \"Repor 1, Tudo ou Voltar?\"")
          
          if i == 10:
               time.sleep(0.1)
               pyautogui.press('enter')
          #pyautogui.write(str(i) + ', ')
   
 
def main():
    time.sleep(3)
    texto()
 
main()


"""

BI1_Geral, BI2_Geral, BI3_Geral, BI4_Geral, BI5_Geral, BI6_Geral, BI7_Geral, BI8_Geral, BI9_Geral, BI10_Geral, 
BI11_Geral, BI12_Geral, BI13_Geral, BI14_Geral, BI15_Geral, BI16_Geral, BI17_Geral, BI18_Geral, BI19_Geral, BI20_Geral, 

Maquina Geral = (SigmaG, Q, δ, Base, {}, ∆)
SigmaG = {
          <Manutenção>, (Identidade Válida), (Identidade Inválida), <Voltar>, <Reposição>, <Repor 1>, <Repor Tudo>, <Comprar>, <Cartão>, <Dinheiro>,
          <1>, <2>, <3>, <4>, <5>, <6>, <7>, <8>, <9>, <10>, <11>, <12>, <13>, <14>, <15>, <16>, <17>, <18>, <19>, <20>,
          (Reposto 1 1), (Reposto 1 2), (Reposto 1 3), (Reposto 1 4), (Reposto 1 5), (Reposto 1 6), (Reposto 1 7), (Reposto 1 8), (Reposto 1 9), (Reposto 1 10),
          (Reposto 1 11), (Reposto 1 12), (Reposto 1 13), (Reposto 1 14), (Reposto 1 15), (Reposto 1 16), (Reposto 1 17), (Reposto 1 18), (Reposto 1 19), (Reposto 1 20),
          (Reposto Tudo 1), (Reposto Tudo 2), (Reposto Tudo 3), (Reposto Tudo 4), (Reposto Tudo 5), (Reposto Tudo 6), (Reposto Tudo 7), (Reposto Tudo 8), (Reposto Tudo 9), (Reposto Tudo 10),
          (Reposto Tudo 11), (Reposto Tudo 12), (Reposto Tudo 13), (Reposto Tudo 14), (Reposto Tudo 15), (Reposto Tudo 16), (Reposto Tudo 17), (Reposto Tudo 18), (Reposto Tudo 19), (Reposto Tudo 20),
          (Sem Estoque 1), (Sem Estoque 2), (Sem Estoque 3), (Sem Estoque 4), (Sem Estoque 5), (Sem Estoque 6), (Sem Estoque 7), (Sem Estoque 8), (Sem Estoque 9), (Sem Estoque 10),
          (Sem Estoque 11), (Sem Estoque 12), (Sem Estoque 13), (Sem Estoque 14), (Sem Estoque 15), (Sem Estoque 16), (Sem Estoque 17), (Sem Estoque 18), (Sem Estoque 19), (Sem Estoque 20),
          (Com Estoque 1), (Com Estoque 2), (Com Estoque 3), (Com Estoque 4), (Com Estoque 5), (Com Estoque 6), (Com Estoque 7), (Com Estoque 8), (Com Estoque 9), (Com Estoque 10),
          (Com Estoque 11), (Com Estoque 12), (Com Estoque 13), (Com Estoque 14), (Com Estoque 15), (Com Estoque 16), (Com Estoque 17), (Com Estoque 18), (Com Estoque 19), (Com Estoque 20),
          (Falha 1), (Falha 2), (Falha 3), (Falha 4), (Falha 5), (Falha 6), (Falha 7), (Falha 8), (Falha 9), (Falha 10),
          (Falha 11), (Falha 12), (Falha 13), (Falha 14), (Falha 15), (Falha 16), (Falha 17), (Falha 18), (Falha 19), (Falha 20),
          (Aceito 1), (Aceito 2), (Aceito 3), (Aceito 4), (Aceito 5), (Aceito 6), (Aceito 7), (Aceito 8), (Aceito 9), (Aceito 10),
          (Aceito 11), (Aceito 12), (Aceito 13), (Aceito 14), (Aceito 15), (Aceito 16), (Aceito 17), (Aceito 18), (Aceito 19), (Aceito 20)
          }
Q = {
     Base, Manutenção Verificação, Manutenção, Reposição Verificação, Reposição, Venda,
     Reposição 1, Reposição 2, Reposição 3, Reposição 4, Reposição 5, Reposição 6, Reposição 7, Reposição 8, Reposição 9, Reposição 10, 
     Reposição 11, Reposição 12, Reposição 13, Reposição 14, Reposição 15, Reposição 16, Reposição 17, Reposição 18, Reposição 19, Reposição 20, 
     Reposto 1 1, Reposto 1 2, Reposto 1 3, Reposto 1 4, Reposto 1 5, Reposto 1 6, Reposto 1 7, Reposto 1 8, Reposto 1 9, Reposto 1 10, 
     Reposto 1 11, Reposto 1 12, Reposto 1 13, Reposto 1 14, Reposto 1 15, Reposto 1 16, Reposto 1 17, Reposto 1 18, Reposto 1 19, Reposto 1 20, 
     Reposto Tudo 1, Reposto Tudo 2, Reposto Tudo 3, Reposto Tudo 4, Reposto Tudo 5, Reposto Tudo 6, Reposto Tudo 7, Reposto Tudo 8, Reposto Tudo 9, Reposto Tudo 10, 
     Reposto Tudo 11, Reposto Tudo 12, Reposto Tudo 13, Reposto Tudo 14, Reposto Tudo 15, Reposto Tudo 16, Reposto Tudo 17, Reposto Tudo 18, Reposto Tudo 19, Reposto Tudo 20, 
     Venda 1, Venda 2, Venda 3, Venda 4, Venda 5, Venda 6, Venda 7, Venda 8, Venda 9, Venda 10, 
     Venda 11, Venda 12, Venda 13, Venda 14, Venda 15, Venda 16, Venda 17, Venda 18, Venda 19, Venda 20, 
     Método Pagamento 1, Método Pagamento 2, Método Pagamento 3, Método Pagamento 4, Método Pagamento 5, Método Pagamento 6, Método Pagamento 7, Método Pagamento 8, Método Pagamento 9, Método Pagamento 10, 
     Método Pagamento 11, Método Pagamento 12, Método Pagamento 13, Método Pagamento 14, Método Pagamento 15, Método Pagamento 16, Método Pagamento 17, Método Pagamento 18, Método Pagamento 19, Método Pagamento 20, 
     Verificação Pagamento 1, Verificação Pagamento 2, Verificação Pagamento 3, Verificação Pagamento 4, Verificação Pagamento 5, Verificação Pagamento 6, Verificação Pagamento 7, Verificação Pagamento 8, Verificação Pagamento 9, Verificação Pagamento 10, 
     Verificação Pagamento 11, Verificação Pagamento 12, Verificação Pagamento 13, Verificação Pagamento 14, Verificação Pagamento 15, Verificação Pagamento 16, Verificação Pagamento 17, Verificação Pagamento 18, Verificação Pagamento 19, Verificação Pagamento 20
     }
     
δ = {
     Base                     x <Manutenção>           > Manutenção Verificação      x [Verificar Identificação],
     Manutenção Verificação   x (Identidade Inválida)  > Base                        x "Id inválida, tente novamente",
     Manutenção Verificação   x (Identidade Válida)    > Manutenção                  x "Maquina desabilitada para manutenção",
     Manutenção               x <Voltar>               > Base                        x "Voltando a operação normal",
     Base                     x <Reposição>            > Reposição Verificação       x ε,
     Reposição Verificação    x (Identidade Invalida)  > Base                        x "Id inválida, tente novamente",
     Reposição Verificação    x (Identidade Válida)    > Reposição                   x "Digite o ID do produto",
     Reposição                x <Voltar>               > Base                        x "Voltando a operação normal",
     Reposição                x <1>                    > Reposição 1                 x "Repor 1, Tudo ou Voltar?",
     Reposição                x <2>                    > Reposição 2                 x "Repor 1, Tudo ou Voltar?",
     Reposição                x <3>                    > Reposição 3                 x "Repor 1, Tudo ou Voltar?",
     Reposição                x <4>                    > Reposição 4                 x "Repor 1, Tudo ou Voltar?",
     Reposição                x <5>                    > Reposição 5                 x "Repor 1, Tudo ou Voltar?",
     Reposição                x <6>                    > Reposição 6                 x "Repor 1, Tudo ou Voltar?",
     Reposição                x <7>                    > Reposição 7                 x "Repor 1, Tudo ou Voltar?",
     Reposição                x <8>                    > Reposição 8                 x "Repor 1, Tudo ou Voltar?",
     Reposição                x <9>                    > Reposição 9                 x "Repor 1, Tudo ou Voltar?",
     Reposição                x <10>                   > Reposição 10                x "Repor 1, Tudo ou Voltar?",
     Reposição                x <11>                   > Reposição 11                x "Repor 1, Tudo ou Voltar?",
     Reposição                x <12>                   > Reposição 12                x "Repor 1, Tudo ou Voltar?",
     Reposição                x <13>                   > Reposição 13                x "Repor 1, Tudo ou Voltar?",
     Reposição                x <14>                   > Reposição 14                x "Repor 1, Tudo ou Voltar?",
     Reposição                x <15>                   > Reposição 15                x "Repor 1, Tudo ou Voltar?",
     Reposição                x <16>                   > Reposição 16                x "Repor 1, Tudo ou Voltar?",
     Reposição                x <17>                   > Reposição 17                x "Repor 1, Tudo ou Voltar?",
     Reposição                x <18>                   > Reposição 18                x "Repor 1, Tudo ou Voltar?",
     Reposição                x <19>                   > Reposição 19                x "Repor 1, Tudo ou Voltar?",
     Reposição                x <20>                   > Reposição 20                x "Repor 1, Tudo ou Voltar?",
     Reposição 1              x <Repor 1>              > Reposto 1 1                 x "Reposto 1 Item" [Repor 1 1],
     Reposição 2              x <Repor 1>              > Reposto 1 2                 x "Reposto 1 Item" [Repor 1 2],
     Reposição 3              x <Repor 1>              > Reposto 1 3                 x "Reposto 1 Item" [Repor 1 3],
     Reposição 4              x <Repor 1>              > Reposto 1 4                 x "Reposto 1 Item" [Repor 1 4],
     Reposição 5              x <Repor 1>              > Reposto 1 5                 x "Reposto 1 Item" [Repor 1 5],
     Reposição 6              x <Repor 1>              > Reposto 1 6                 x "Reposto 1 Item" [Repor 1 6],
     Reposição 7              x <Repor 1>              > Reposto 1 7                 x "Reposto 1 Item" [Repor 1 7],
     Reposição 8              x <Repor 1>              > Reposto 1 8                 x "Reposto 1 Item" [Repor 1 8],
     Reposição 9              x <Repor 1>              > Reposto 1 9                 x "Reposto 1 Item" [Repor 1 9],
     Reposição 10             x <Repor 1>              > Reposto 1 10                x "Reposto 1 Item" [Repor 1 10],
     Reposição 11             x <Repor 1>              > Reposto 1 11                x "Reposto 1 Item" [Repor 1 11],
     Reposição 12             x <Repor 1>              > Reposto 1 12                x "Reposto 1 Item" [Repor 1 12],
     Reposição 13             x <Repor 1>              > Reposto 1 13                x "Reposto 1 Item" [Repor 1 13],
     Reposição 14             x <Repor 1>              > Reposto 1 14                x "Reposto 1 Item" [Repor 1 14],
     Reposição 15             x <Repor 1>              > Reposto 1 15                x "Reposto 1 Item" [Repor 1 15],
     Reposição 16             x <Repor 1>              > Reposto 1 16                x "Reposto 1 Item" [Repor 1 16],
     Reposição 17             x <Repor 1>              > Reposto 1 17                x "Reposto 1 Item" [Repor 1 17],
     Reposição 18             x <Repor 1>              > Reposto 1 18                x "Reposto 1 Item" [Repor 1 18],
     Reposição 19             x <Repor 1>              > Reposto 1 19                x "Reposto 1 Item" [Repor 1 19],
     Reposição 20             x <Repor 1>              > Reposto 1 20                x "Reposto 1 Item" [Repor 1 19],
     Reposição 1              x <Repor Tudo>           > Reposto Tudo 1              x "Reposto todos Itens" [Repor Tudo 1],
     Reposição 2              x <Repor Tudo>           > Reposto Tudo 2              x "Reposto todos Itens" [Repor Tudo 2],
     Reposição 3              x <Repor Tudo>           > Reposto Tudo 3              x "Reposto todos Itens" [Repor Tudo 3],
     Reposição 4              x <Repor Tudo>           > Reposto Tudo 4              x "Reposto todos Itens" [Repor Tudo 4],
     Reposição 5              x <Repor Tudo>           > Reposto Tudo 5              x "Reposto todos Itens" [Repor Tudo 5],
     Reposição 6              x <Repor Tudo>           > Reposto Tudo 6              x "Reposto todos Itens" [Repor Tudo 6],
     Reposição 7              x <Repor Tudo>           > Reposto Tudo 7              x "Reposto todos Itens" [Repor Tudo 7],
     Reposição 8              x <Repor Tudo>           > Reposto Tudo 8              x "Reposto todos Itens" [Repor Tudo 8],
     Reposição 9              x <Repor Tudo>           > Reposto Tudo 9              x "Reposto todos Itens" [Repor Tudo 9],
     Reposição 10             x <Repor Tudo>           > Reposto Tudo 10             x "Reposto todos Itens" [Repor Tudo 10],
     Reposição 11             x <Repor Tudo>           > Reposto Tudo 11             x "Reposto todos Itens" [Repor Tudo 11],
     Reposição 12             x <Repor Tudo>           > Reposto Tudo 12             x "Reposto todos Itens" [Repor Tudo 12],
     Reposição 13             x <Repor Tudo>           > Reposto Tudo 13             x "Reposto todos Itens" [Repor Tudo 13],
     Reposição 14             x <Repor Tudo>           > Reposto Tudo 14             x "Reposto todos Itens" [Repor Tudo 14],
     Reposição 15             x <Repor Tudo>           > Reposto Tudo 15             x "Reposto todos Itens" [Repor Tudo 15],
     Reposição 16             x <Repor Tudo>           > Reposto Tudo 16             x "Reposto todos Itens" [Repor Tudo 16],
     Reposição 17             x <Repor Tudo>           > Reposto Tudo 17             x "Reposto todos Itens" [Repor Tudo 17],
     Reposição 18             x <Repor Tudo>           > Reposto Tudo 18             x "Reposto todos Itens" [Repor Tudo 18],
     Reposição 19             x <Repor Tudo>           > Reposto Tudo 19             x "Reposto todos Itens" [Repor Tudo 19],
     Reposição 20             x <Repor Tudo>           > Reposto Tudo 20             x "Reposto todos Itens" [Repor Tudo 19],
     Reposto 1 1              x (Reposto 1 1)          > Base                        x ε,
     Reposto 1 2              x (Reposto 1 2)          > Base                        x ε,
     Reposto 1 3              x (Reposto 1 3)          > Base                        x ε,
     Reposto 1 4              x (Reposto 1 4)          > Base                        x ε,
     Reposto 1 5              x (Reposto 1 5)          > Base                        x ε,
     Reposto 1 6              x (Reposto 1 6)          > Base                        x ε,
     Reposto 1 7              x (Reposto 1 7)          > Base                        x ε,
     Reposto 1 8              x (Reposto 1 8)          > Base                        x ε,
     Reposto 1 9              x (Reposto 1 9)          > Base                        x ε,
     Reposto 1 10             x (Reposto 1 10)         > Base                        x ε,
     Reposto 1 11             x (Reposto 1 11)         > Base                        x ε,
     Reposto 1 12             x (Reposto 1 12)         > Base                        x ε,
     Reposto 1 13             x (Reposto 1 13)         > Base                        x ε,
     Reposto 1 14             x (Reposto 1 14)         > Base                        x ε,
     Reposto 1 15             x (Reposto 1 15)         > Base                        x ε,
     Reposto 1 16             x (Reposto 1 16)         > Base                        x ε,
     Reposto 1 17             x (Reposto 1 17)         > Base                        x ε,
     Reposto 1 18             x (Reposto 1 18)         > Base                        x ε,
     Reposto 1 19             x (Reposto 1 19)         > Base                        x ε,
     Reposto 1 20             x (Reposto 1 20)         > Base                        x ε,
     Reposto Tudo 1           x (Reposto Tudo 1)       > Base                        x ε,
     Reposto Tudo 2           x (Reposto Tudo 2)       > Base                        x ε,
     Reposto Tudo 3           x (Reposto Tudo 3)       > Base                        x ε,
     Reposto Tudo 4           x (Reposto Tudo 4)       > Base                        x ε,
     Reposto Tudo 5           x (Reposto Tudo 5)       > Base                        x ε,
     Reposto Tudo 6           x (Reposto Tudo 6)       > Base                        x ε,
     Reposto Tudo 7           x (Reposto Tudo 7)       > Base                        x ε,
     Reposto Tudo 8           x (Reposto Tudo 8)       > Base                        x ε,
     Reposto Tudo 9           x (Reposto Tudo 9)       > Base                        x ε,
     Reposto Tudo 10          x (Reposto Tudo 10)      > Base                        x ε,
     Reposto Tudo 11          x (Reposto Tudo 11)      > Base                        x ε,
     Reposto Tudo 12          x (Reposto Tudo 12)      > Base                        x ε,
     Reposto Tudo 13          x (Reposto Tudo 13)      > Base                        x ε,
     Reposto Tudo 14          x (Reposto Tudo 14)      > Base                        x ε,
     Reposto Tudo 15          x (Reposto Tudo 15)      > Base                        x ε,
     Reposto Tudo 16          x (Reposto Tudo 16)      > Base                        x ε,
     Reposto Tudo 17          x (Reposto Tudo 17)      > Base                        x ε,
     Reposto Tudo 18          x (Reposto Tudo 18)      > Base                        x ε,
     Reposto Tudo 19          x (Reposto Tudo 19)      > Base                        x ε,
     Reposto Tudo 20          x (Reposto Tudo 20)      > Base                        x ε,
     Base                     x <Comprar>              > Venda                       x "Qual ID do produto?",
     Venda                    x <Voltar>               > Base                        x "Voltando Menu Inicial",
     Venda                    x <1>                    > Venda 1                     x "Verificando estoque" [Verificar estoque 1],
     Venda                    x <2>                    > Venda 2                     x "Verificando estoque" [Verificar estoque 2],
     Venda                    x <3>                    > Venda 3                     x "Verificando estoque" [Verificar estoque 3],
     Venda                    x <4>                    > Venda 4                     x "Verificando estoque" [Verificar estoque 4],
     Venda                    x <5>                    > Venda 5                     x "Verificando estoque" [Verificar estoque 5],
     Venda                    x <6>                    > Venda 6                     x "Verificando estoque" [Verificar estoque 6],
     Venda                    x <7>                    > Venda 7                     x "Verificando estoque" [Verificar estoque 7],
     Venda                    x <8>                    > Venda 8                     x "Verificando estoque" [Verificar estoque 8],
     Venda                    x <9>                    > Venda 9                     x "Verificando estoque" [Verificar estoque 9],
     Venda                    x <10>                   > Venda 10                    x "Verificando estoque" [Verificar estoque 10],
     Venda                    x <11>                   > Venda 11                    x "Verificando estoque" [Verificar estoque 11],
     Venda                    x <12>                   > Venda 12                    x "Verificando estoque" [Verificar estoque 12],
     Venda                    x <13>                   > Venda 13                    x "Verificando estoque" [Verificar estoque 13],
     Venda                    x <14>                   > Venda 14                    x "Verificando estoque" [Verificar estoque 14],
     Venda                    x <15>                   > Venda 15                    x "Verificando estoque" [Verificar estoque 15],
     Venda                    x <16>                   > Venda 16                    x "Verificando estoque" [Verificar estoque 16],
     Venda                    x <17>                   > Venda 17                    x "Verificando estoque" [Verificar estoque 17],
     Venda                    x <18>                   > Venda 18                    x "Verificando estoque" [Verificar estoque 18],
     Venda                    x <19>                   > Venda 19                    x "Verificando estoque" [Verificar estoque 19],
     Venda                    x <20>                   > Venda 20                    x "Verificando estoque" [Verificar estoque 20],
     Venda 1                  x (Sem Estoque 1)        > Venda                       x "Estoque vazio, escolha outro item",
     Venda 2                  x (Sem Estoque 2)        > Venda                       x "Estoque vazio, escolha outro item",
     Venda 3                  x (Sem Estoque 3)        > Venda                       x "Estoque vazio, escolha outro item",
     Venda 4                  x (Sem Estoque 4)        > Venda                       x "Estoque vazio, escolha outro item",
     Venda 5                  x (Sem Estoque 5)        > Venda                       x "Estoque vazio, escolha outro item",
     Venda 6                  x (Sem Estoque 6)        > Venda                       x "Estoque vazio, escolha outro item",
     Venda 7                  x (Sem Estoque 7)        > Venda                       x "Estoque vazio, escolha outro item",
     Venda 8                  x (Sem Estoque 8)        > Venda                       x "Estoque vazio, escolha outro item",
     Venda 9                  x (Sem Estoque 9)        > Venda                       x "Estoque vazio, escolha outro item",
     Venda 10                 x (Sem Estoque 10)       > Venda                       x "Estoque vazio, escolha outro item",
     Venda 11                 x (Sem Estoque 11)       > Venda                       x "Estoque vazio, escolha outro item",
     Venda 12                 x (Sem Estoque 12)       > Venda                       x "Estoque vazio, escolha outro item",
     Venda 13                 x (Sem Estoque 13)       > Venda                       x "Estoque vazio, escolha outro item",
     Venda 14                 x (Sem Estoque 14)       > Venda                       x "Estoque vazio, escolha outro item",
     Venda 15                 x (Sem Estoque 15)       > Venda                       x "Estoque vazio, escolha outro item",
     Venda 16                 x (Sem Estoque 16)       > Venda                       x "Estoque vazio, escolha outro item",
     Venda 17                 x (Sem Estoque 17)       > Venda                       x "Estoque vazio, escolha outro item",
     Venda 18                 x (Sem Estoque 18)       > Venda                       x "Estoque vazio, escolha outro item",
     Venda 19                 x (Sem Estoque 19)       > Venda                       x "Estoque vazio, escolha outro item",
     Venda 20                 x (Sem Estoque 20)       > Venda                       x "Estoque vazio, escolha outro item",
     Venda 1                  x (Com Estoque 1)        > Método Pagamento 1          x "Qual metodo de pagamento?",
     Venda 2                  x (Com Estoque 2)        > Método Pagamento 2          x "Qual metodo de pagamento?",
     Venda 3                  x (Com Estoque 3)        > Método Pagamento 3          x "Qual metodo de pagamento?",
     Venda 4                  x (Com Estoque 4)        > Método Pagamento 4          x "Qual metodo de pagamento?",
     Venda 5                  x (Com Estoque 5)        > Método Pagamento 5          x "Qual metodo de pagamento?",
     Venda 6                  x (Com Estoque 6)        > Método Pagamento 6          x "Qual metodo de pagamento?",
     Venda 7                  x (Com Estoque 7)        > Método Pagamento 7          x "Qual metodo de pagamento?",
     Venda 8                  x (Com Estoque 8)        > Método Pagamento 8          x "Qual metodo de pagamento?",
     Venda 9                  x (Com Estoque 9)        > Método Pagamento 9          x "Qual metodo de pagamento?",
     Venda 10                 x (Com Estoque 10)       > Método Pagamento 10         x "Qual metodo de pagamento?",
     Venda 11                 x (Com Estoque 11)       > Método Pagamento 11         x "Qual metodo de pagamento?",
     Venda 12                 x (Com Estoque 12)       > Método Pagamento 12         x "Qual metodo de pagamento?",
     Venda 13                 x (Com Estoque 13)       > Método Pagamento 13         x "Qual metodo de pagamento?",
     Venda 14                 x (Com Estoque 14)       > Método Pagamento 14         x "Qual metodo de pagamento?",
     Venda 15                 x (Com Estoque 15)       > Método Pagamento 15         x "Qual metodo de pagamento?",
     Venda 16                 x (Com Estoque 16)       > Método Pagamento 16         x "Qual metodo de pagamento?",
     Venda 17                 x (Com Estoque 17)       > Método Pagamento 17         x "Qual metodo de pagamento?",
     Venda 18                 x (Com Estoque 18)       > Método Pagamento 18         x "Qual metodo de pagamento?",
     Venda 19                 x (Com Estoque 19)       > Método Pagamento 19         x "Qual metodo de pagamento?",
     Venda 20                 x (Com Estoque 20)       > Método Pagamento 20         x "Qual metodo de pagamento?",
     Método Pagamento 1       x <Cartão>               > Verificação Pagamento 1     x [Verificar pagamento 1],
     Método Pagamento 2       x <Cartão>               > Verificação Pagamento 2     x [Verificar pagamento 2],
     Método Pagamento 3       x <Cartão>               > Verificação Pagamento 3     x [Verificar pagamento 3],
     Método Pagamento 4       x <Cartão>               > Verificação Pagamento 4     x [Verificar pagamento 4],
     Método Pagamento 5       x <Cartão>               > Verificação Pagamento 5     x [Verificar pagamento 5],
     Método Pagamento 6       x <Cartão>               > Verificação Pagamento 6     x [Verificar pagamento 6],
     Método Pagamento 7       x <Cartão>               > Verificação Pagamento 7     x [Verificar pagamento 7],
     Método Pagamento 8       x <Cartão>               > Verificação Pagamento 8     x [Verificar pagamento 8],
     Método Pagamento 9       x <Cartão>               > Verificação Pagamento 9     x [Verificar pagamento 9],
     Método Pagamento 10      x <Cartão>               > Verificação Pagamento 10    x [Verificar pagamento 10],
     Método Pagamento 11      x <Cartão>               > Verificação Pagamento 11    x [Verificar pagamento 11],
     Método Pagamento 12      x <Cartão>               > Verificação Pagamento 12    x [Verificar pagamento 12],
     Método Pagamento 13      x <Cartão>               > Verificação Pagamento 13    x [Verificar pagamento 13],
     Método Pagamento 14      x <Cartão>               > Verificação Pagamento 14    x [Verificar pagamento 14],
     Método Pagamento 15      x <Cartão>               > Verificação Pagamento 15    x [Verificar pagamento 15],
     Método Pagamento 16      x <Cartão>               > Verificação Pagamento 16    x [Verificar pagamento 16],
     Método Pagamento 17      x <Cartão>               > Verificação Pagamento 17    x [Verificar pagamento 17],
     Método Pagamento 18      x <Cartão>               > Verificação Pagamento 18    x [Verificar pagamento 18],
     Método Pagamento 19      x <Cartão>               > Verificação Pagamento 19    x [Verificar pagamento 19],
     Método Pagamento 20      x <Cartão>               > Verificação Pagamento 20    x [Verificar pagamento 20],
     Método Pagamento 1       x <Dinheiro>             > Verificação Pagamento 1     x [Verificar pagamento 1],
     Método Pagamento 2       x <Dinheiro>             > Verificação Pagamento 2     x [Verificar pagamento 2],
     Método Pagamento 3       x <Dinheiro>             > Verificação Pagamento 3     x [Verificar pagamento 3],
     Método Pagamento 4       x <Dinheiro>             > Verificação Pagamento 4     x [Verificar pagamento 4],
     Método Pagamento 5       x <Dinheiro>             > Verificação Pagamento 5     x [Verificar pagamento 5],
     Método Pagamento 6       x <Dinheiro>             > Verificação Pagamento 6     x [Verificar pagamento 6],
     Método Pagamento 7       x <Dinheiro>             > Verificação Pagamento 7     x [Verificar pagamento 7],
     Método Pagamento 8       x <Dinheiro>             > Verificação Pagamento 8     x [Verificar pagamento 8],
     Método Pagamento 9       x <Dinheiro>             > Verificação Pagamento 9     x [Verificar pagamento 9],
     Método Pagamento 10      x <Dinheiro>             > Verificação Pagamento 10    x [Verificar pagamento 10],
     Método Pagamento 11      x <Dinheiro>             > Verificação Pagamento 11    x [Verificar pagamento 11],
     Método Pagamento 12      x <Dinheiro>             > Verificação Pagamento 12    x [Verificar pagamento 12],
     Método Pagamento 13      x <Dinheiro>             > Verificação Pagamento 13    x [Verificar pagamento 13],
     Método Pagamento 14      x <Dinheiro>             > Verificação Pagamento 14    x [Verificar pagamento 14],
     Método Pagamento 15      x <Dinheiro>             > Verificação Pagamento 15    x [Verificar pagamento 15],
     Método Pagamento 16      x <Dinheiro>             > Verificação Pagamento 16    x [Verificar pagamento 16],
     Método Pagamento 17      x <Dinheiro>             > Verificação Pagamento 17    x [Verificar pagamento 17],
     Método Pagamento 18      x <Dinheiro>             > Verificação Pagamento 18    x [Verificar pagamento 18],
     Método Pagamento 19      x <Dinheiro>             > Verificação Pagamento 19    x [Verificar pagamento 19],
     Método Pagamento 20      x <Dinheiro>             > Verificação Pagamento 20    x [Verificar pagamento 20],
     Verificação Pagamento 1  x (Falha 1)              > Venda                       x "Falha no pagamento",
     Verificação Pagamento 2  x (Falha 2)              > Venda                       x "Falha no pagamento",
     Verificação Pagamento 3  x (Falha 3)              > Venda                       x "Falha no pagamento",
     Verificação Pagamento 4  x (Falha 4)              > Venda                       x "Falha no pagamento",
     Verificação Pagamento 5  x (Falha 5)              > Venda                       x "Falha no pagamento",
     Verificação Pagamento 6  x (Falha 6)              > Venda                       x "Falha no pagamento",
     Verificação Pagamento 7  x (Falha 7)              > Venda                       x "Falha no pagamento",
     Verificação Pagamento 8  x (Falha 8)              > Venda                       x "Falha no pagamento",
     Verificação Pagamento 9  x (Falha 9)              > Venda                       x "Falha no pagamento",
     Verificação Pagamento 10 x (Falha 10)             > Venda                       x "Falha no pagamento",
     Verificação Pagamento 11 x (Falha 11)             > Venda                       x "Falha no pagamento",
     Verificação Pagamento 12 x (Falha 12)             > Venda                       x "Falha no pagamento",
     Verificação Pagamento 13 x (Falha 13)             > Venda                       x "Falha no pagamento",
     Verificação Pagamento 14 x (Falha 14)             > Venda                       x "Falha no pagamento",
     Verificação Pagamento 15 x (Falha 15)             > Venda                       x "Falha no pagamento",
     Verificação Pagamento 16 x (Falha 16)             > Venda                       x "Falha no pagamento",
     Verificação Pagamento 17 x (Falha 17)             > Venda                       x "Falha no pagamento",
     Verificação Pagamento 18 x (Falha 18)             > Venda                       x "Falha no pagamento",
     Verificação Pagamento 19 x (Falha 19)             > Venda                       x "Falha no pagamento",
     Verificação Pagamento 20 x (Falha 20)             > Venda                       x "Falha no pagamento",
     Verificação Pagamento 1  x (Aceito 1)             > Base                        x "Pagamento aceito, retire seu produto",
     Verificação Pagamento 2  x (Aceito 2)             > Base                        x "Pagamento aceito, retire seu produto",
     Verificação Pagamento 3  x (Aceito 3)             > Base                        x "Pagamento aceito, retire seu produto",
     Verificação Pagamento 4  x (Aceito 4)             > Base                        x "Pagamento aceito, retire seu produto",
     Verificação Pagamento 5  x (Aceito 5)             > Base                        x "Pagamento aceito, retire seu produto",
     Verificação Pagamento 6  x (Aceito 6)             > Base                        x "Pagamento aceito, retire seu produto",
     Verificação Pagamento 7  x (Aceito 7)             > Base                        x "Pagamento aceito, retire seu produto",
     Verificação Pagamento 8  x (Aceito 8)             > Base                        x "Pagamento aceito, retire seu produto",
     Verificação Pagamento 9  x (Aceito 9)             > Base                        x "Pagamento aceito, retire seu produto",
     Verificação Pagamento 10 x (Aceito 10)            > Base                        x "Pagamento aceito, retire seu produto",
     Verificação Pagamento 11 x (Aceito 11)            > Base                        x "Pagamento aceito, retire seu produto",
     Verificação Pagamento 12 x (Aceito 12)            > Base                        x "Pagamento aceito, retire seu produto",
     Verificação Pagamento 13 x (Aceito 13)            > Base                        x "Pagamento aceito, retire seu produto",
     Verificação Pagamento 14 x (Aceito 14)            > Base                        x "Pagamento aceito, retire seu produto",
     Verificação Pagamento 15 x (Aceito 15)            > Base                        x "Pagamento aceito, retire seu produto",
     Verificação Pagamento 16 x (Aceito 16)            > Base                        x "Pagamento aceito, retire seu produto",
     Verificação Pagamento 17 x (Aceito 17)            > Base                        x "Pagamento aceito, retire seu produto",
     Verificação Pagamento 18 x (Aceito 18)            > Base                        x "Pagamento aceito, retire seu produto",
     Verificação Pagamento 19 x (Aceito 19)            > Base                        x "Pagamento aceito, retire seu produto",
     Verificação Pagamento 20 x (Aceito 20)            > Base                        x "Pagamento aceito, retire seu produto"
     }

∆ = {
     ε, [Verificar Identificação], "Id inválida, tente novamente", "Maquina desabilitada para manutenção", "Voltando a operação normal", "Digite o ID do produto", "Repor 1, Tudo ou Voltar?", "Reposto 1 Item", "Reposto todos Itens",
     "Qual ID do produto?", "Voltando Menu Inicial", "Verificando estoque", "Estoque vazio, escolha outro item", "Qual metodo de pagamento?", "Falha no pagamento", "Pagamento aceito, retire seu produto",
     [Repor 1 1], [Repor 1 2], [Repor 1 3], [Repor 1 4], [Repor 1 5], [Repor 1 6], [Repor 1 7], [Repor 1 8], [Repor 1 9], [Repor 1 10], 
     [Repor 1 11], [Repor 1 12], [Repor 1 13], [Repor 1 14], [Repor 1 15], [Repor 1 16], [Repor 1 17], [Repor 1 18], [Repor 1 19], [Repor 1 20], 
     [Repor Tudo 1], [Repor Tudo 2], [Repor Tudo 3], [Repor Tudo 4], [Repor Tudo 5], [Repor Tudo 6], [Repor Tudo 7], [Repor Tudo 8], [Repor Tudo 9], [Repor Tudo 10], 
     [Repor Tudo 11], [Repor Tudo 12], [Repor Tudo 13], [Repor Tudo 14], [Repor Tudo 15], [Repor Tudo 16], [Repor Tudo 17], [Repor Tudo 18], [Repor Tudo 19], [Repor Tudo 20], 
     [Verificar estoque 1], [Verificar estoque 2], [Verificar estoque 3], [Verificar estoque 4], [Verificar estoque 5], [Verificar estoque 6], [Verificar estoque 7], [Verificar estoque 8], [Verificar estoque 9], [Verificar estoque 10], 
     [Verificar estoque 11], [Verificar estoque 12], [Verificar estoque 13], [Verificar estoque 14], [Verificar estoque 15], [Verificar estoque 16], [Verificar estoque 17], [Verificar estoque 18], [Verificar estoque 19], [Verificar estoque 20], 
     [Verificar pagamento 1], [Verificar pagamento 2], [Verificar pagamento 3], [Verificar pagamento 4], [Verificar pagamento 5], [Verificar pagamento 6], [Verificar pagamento 7], [Verificar pagamento 8], [Verificar pagamento 9], [Verificar pagamento 10], 
     [Verificar pagamento 11], [Verificar pagamento 12], [Verificar pagamento 13], [Verificar pagamento 14], [Verificar pagamento 15], [Verificar pagamento 16], [Verificar pagamento 17], [Verificar pagamento 18], [Verificar pagamento 19], [Verificar pagamento 20]
     }
"""
