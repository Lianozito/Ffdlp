from UI.signature import show_signature
from UI.colors import RED, BLUE, RESET

def main():
    show_signature()
    
    while True:
     print('1 - Download youtube video?')
     print('2 - Cut video!')
     print('3 - Convert video to audio or download audio from youtube?')
     print('4 - Close program!')

     choice = (input('Choose an option: ')).strip()
    
     if choice == '1':
        print(f'{BLUE}Back to main menu: type "back" {RESET}')
        while True:
             link_youtube = input('Please paste your YouTube link: ').strip()
             #sistema para verificar se o link funciona e é aceito pelo yt-dlp.
             #sistema para seleção de qualidade de video e audio disponiveis!
             #sistema para escolha de formato de video e audio disponiveis!
             if link_youtube in ('back', 'Back', 'BACK'):
                break
        

     elif choice == '2':
        while True:
         #sistema para abrir pasta do video!
         #sistema para chamar o ffmpeg!
         #sistema para adicionar inicio e fim do corte!
         pass

     elif choice == '3':
        while True:
             print('1 - Convert video to audio!')
             #sistema para converter video para audio usando o ffmpeg!
             print('2 - Download audio from youtube!')
             #sistema para baixar audio do youtube usando o yt-dlp!
             print('3 - Back to main menu!')
             audio = input('Choose an option: ').strip()
             if audio == '1':
                 #sistema para abrir pasta do video!
                 #sistema para chamar o ffmpeg!
                 pass
             elif audio == '2':
                 link_youtube = input('Please paste your YouTube link: ').strip()
                 print('Verifying link...')
                 #sistema para verificar se o link funciona e é aceito pelo yt-dlp.
                 #sistema para baixar audio do youtube usando o yt-dlp!
             elif audio == '3':
                 break
             else:
                 print(f'{RED}Invalid option, please try again!{RESET}')

     elif choice == '4':
         print('Closing program...')
         #sistema para fechar o programa!
         break
     else:
         print(f'{RED}Invalid option, please try again!{RESET}')
    
if __name__ == '__main__':
    main()