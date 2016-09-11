# -*- coding: <UTF-8> -*-
def cashMachine(WithdrawValue):
    # Set notes values
    notes = [100.0 , 50.0 , 20.0 , 10.0]
    Withdraw = []
    for NoteValue in notes:
        for NumberNotes in range(int(WithdrawValue // NoteValue)):
            Withdraw.append(NoteValue)
            WithdrawValue = WithdrawValue % NoteValue
    return Withdraw

if __name__ ==  '__main__':
    # Scan In
    try:
        WithdrawValue = float(input())
    # End of file
    except EOFError:
        print("*Fim do arquivo*")
        exit()
    # Null/In values erros
    except:
        print("*Erro de valor nulo*")
        exit()

    if WithdrawValue < 0.0:
        print("*Erro de valor inválido*")
        exit()
    if not (WithdrawValue % 10 == 0):
        print("*Erro de notas indisponíveis*")
        exit()

    print(cashMachine(WithdrawValue))
