from pystyle import Colors, System, Write, Add ,Colorate, Center

class sdt:
    """
    Made By Aboz
    Discord : 3a.b
    """
    def menu(text)-> str:
        """
        set menu str

        exp :
        import sdt
        sdt.menu("YOUR_TEXT\nYOUR_TEXT")

        make sure that you put \n after the text
        """
        lines = text.split('\n')
        processed_text = []
        for line_number, line in enumerate(lines, 1): 
            processed_line = f"«{line_number}» {line}" 
            processed_text.append(processed_line)
        processed_text = '\n'.join(processed_text)
        print(Colorate.Vertical(Colors.blue_to_white,Center.XCenter(processed_text)))
        print("\n"*2)
        return processed_text
    
    def logo()-> str:
        """
        Print your Logo.
        """
        logo = """
╦ ╦┌─┐┌─┐┬─┐  ╔═╗┬ ┬┌─┐┌─┐┬┌─┌─┐┬─┐
║ ║└─┐├┤ ├┬┘  ║  ├─┤├┤ │  ├┴┐├┤ ├┬┘
╚═╝└─┘└─┘┴└─  ╚═╝┴ ┴└─┘└─┘┴ ┴└─┘┴└─v4.\n
⁕ Developed by @_._i on Discord\n\n"""
        print(Colorate.Vertical(Colors.blue_to_white,Center.XCenter(logo)))

    def input(text:str)-> str:
        """
        set input str

        exp :
        import sdt
        sdt.input("YOUR_TEXT")
        """
        Write.Input(text,Colors.blue_to_white,interval=0.01)

    def title(text:str)-> str:
        """
        set title str

        exp :
        import sdt
        sdt.title("YOUR_TEXT")
        """
        System.Title(text)