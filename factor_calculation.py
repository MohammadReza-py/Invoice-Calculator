#imports
import calculator
from rich.console import Console
from rich.prompt import Prompt

console = Console()
prompt = Prompt()

console.rule('[bold yellow]hello')
console.rule('[bold blue]wellcome to program')

add_list = {} # add list the valu e for add to class

def toDecimalFromPercent(percentage: str) -> float:
    if not percentage.isdigit():
        raise ValueError("Input must be numeric characters only.")

    length = len(percentage)

    if length == 1:
        return float(f"0.0{percentage}")
    elif length == 2:
        return float(f"0.{percentage}")
    else:
        return float(f"{percentage[:-2]}.{percentage[-2:]}")

if __name__ == '__main__':
    command = 'run'
    calculation = calculator.CallculationOperation()
    while True:
        console.print('1.calculate | 2.exit')
        command = input('what do you going to did ? ')
        print('loading')
        if command not in ['calculate', 'exit', '1', '2']:
            console.print("I don't understand what you mean. Please ask for something that I can implement",  style='underline red')
            command = prompt.ask('what do you going to did ? ', choices=['calculate', 'exit'])
            print('loading')
    
        if command in ['exit', 2]:
            console.rule('[bold red]goodbye')
            exit()
    
        while command in ['calculate', '1', 'y']:
            try :
                product = console.input('please give , [bold green underline]product name[/] : ')
                number =  int(console.input('please give , [bold green underline]product number[/] : '))
                price = int(console.input('please give , [bold green underline]product price[/] : '))
                discount = toDecimalFromPercent(console.input('please give , [bold green underline]Discount[/] : '))
                print('loading')
                
            except ValueError:
                console.print('please give number and pay in numberly', style='underline red')
            except :
                console.print('Sorry, the app encountered a problem', style='red on white')

            else :
                calculation.addProduct({
                    product: {'price': price, 'discount': discount, 'number': number}
                })
                command = prompt.ask('do you going to continue ? ', choices=['y', 'N'])
                factor = calculation.calculationPay()
                print('loading')

                if command == 'N':
                    print(calculation.tabulateShow(factor['products']))
                    print(f'your total price is: {factor["totalPay"]}$')
                    print('----------------')
                else: print(calculation.tabulateShow(factor['products']))