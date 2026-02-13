from UI.signature import show_signature
from UI.colors import RED, BLUE, RESET, GREEN, YELLOW

def main():
    show_signature()
    
    while True:
     print(f'{GREEN}1 - Download youtube video?{RESET}')
     print(f'{GREEN}2 - Cut video!{RESET}')
     print(f'{GREEN}3 - Convert video to audio or download audio from youtube?{RESET}')
     print(f'{RED}4 - Close program!{RESET}')

     choice = (input('Choose an option: ')).strip()
     
     links_adds = []
    
     while True:
        quantity_string = input('How many videos do you want to download?: ').strip()
        if quantity_string == '':
            print(f'{RED}Invalid quantity, please try again!{RESET}')
            continue
        elif quantity_string.isdigit():
            quantity = int(quantity_string)
            if quantity <= 0:
                print(f'{RED}Invalid quantity, please try again!{RESET}')
                continue
            break
    
     if choice == '1':
        for i in range(quantity):
            print(f'{BLUE}Back to main menu: type "back" {RESET}')
            link_youtube = input(f'Please paste your YouTube link {i+1}: ').strip()
            #sistema para verificar se o link funciona e é aceito pelo yt-dlp.
            links_adds.append(link_youtube)
            if link_youtube.lower() == ('back'):
                 break
            print(f'{YELLOW}Verifying link...{RESET}')
             #sistema para seleção de qualidade de video e audio disponiveis!
             #sistema para escolha de formato de video e audio disponiveis!
        

     elif choice == '2':
        while True:
         #sistema para abrir pasta do video!
         #sistema para chamar o ffmpeg!
         #sistema para adicionar inicio e fim do corte!
         pass

     elif choice == '3':
        while True:
             print(f'{GREEN}1 - Convert video to audio!{RESET}')
             #sistema para converter video para audio usando o ffmpeg!
             print(f'{GREEN}2 - Download audio from youtube!{RESET}')
             #sistema para baixar audio do youtube usando o yt-dlp!
             print(f'{BLUE}3 - Back to main menu!{RESET}')
             audio = input('Choose an option: ').strip()
             if audio == '1':
                 #sistema para abrir pasta do video!
                 #sistema para chamar o ffmpeg!
                 pass
             elif audio == '2':
                 link_youtube = input('Please paste your YouTube link: ').strip()
                 print(f'{YELLOW}Verifying link...{RESET}')
                 #sistema para verificar se o link funciona e é aceito pelo yt-dlp.
                 #sistema para baixar audio do youtube usando o yt-dlp!
             elif audio == '3':
                 break
             else:
                 print(f'{RED}Invalid option, please try again!{RESET}')

     elif choice == '4':
         print(f'{RED}Closing program...{RESET}')
         #sistema para fechar o programa!
         break
     else:
         print(f'{RED}Invalid option, please try again!{RESET}')
    
if __name__ == '__main__':
    main()