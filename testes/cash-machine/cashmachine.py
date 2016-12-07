# -*- coding: <UTF-8> -*-
def cashMachine(WithdrawValue, notes):
    # Set notes values
    Withdraw = []
    for NoteValue in notes:
        for NumberNotes in range(int(WithdrawValue // NoteValue)):
            Withdraw.append(NoteValue)
            WithdrawValue = WithdrawValue % NoteValue
    return Withdraw

if __name__ ==  '__main__':
    notes = [100.0 , 50.0 , 20.0 , 10.0]
    # Scan In
    try:
        WithdrawValue = float(input())
    # End of file
    except EOFError:
        print("*Erro valor nulo*")
        exit()
    # Null/In values erros
    except ValueError:
        print("*Erro de valor inválido*")
        exit()

    if WithdrawValue < 0.0:
        print("*Erro de valor inválido*")
        exit()
    # Check if there are notes to fullfil the withdraw
    if not (WithdrawValue % notes[len(notes) - 1] == 0):
        print("*Erro de notas indisponíveis*")
        exit()

    print(cashMachine(WithdrawValue,notes))
