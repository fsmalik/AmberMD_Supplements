import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-i", "--input", required=True, help='input file // FORMAT --> .pdb')
parser.add_argument("-o", "--output", required=True, help='output file // FORMAT --> .txt')
args = parser.parse_args()

print('\n')
print('                              ..................:..............:.   ....  ..... .............    .............-        ')
print('                            :...................:....        -        ........ ......-........    ......--.....        ')
print('                           =...=...............-...        -            ... ..... .... ... ...  ................       ')
print('                          =...=.........-.....--        --                .......  .-..... ..   .. .......:.-...:      ')
print('                          ...=.........      =-.      --      *+++         ..... . -  ... ..    .. ... ..........      ')
print('                         ...=-.......:.      --    ::   .         **       - .    .    :..    -  ..... ...-.......     ')
print('                        ...+=.......  :     ::::::                 - -     -      -        -        ... ........ .     ')
print('                       ..-.=..:....         :::                    : :     :   . -             -     ......:...  .=    ')
print('                      ....==......   :     -:::                    - :     :    :                    : ......:..  .    ')
print('                     ....:=..-.... -       ::.      .%%%%%  :        :     :   :                     -  ......... .    ')
print('                    .-...==......   -      .    ###%+     %%##             :             *++++       :  ...:........   ')
print('                   ......=-.....    -         ***       **    ** ::       .::    :             ++     - ............   ')
print('                  .. ...=-....      -     . ++*          +++   =+ -.       ::        ...              -   ...... .     ')
print('                 :. ....==....      -     .-++     #####*++++   =    -:     :                         -   -  ...       ')
print('                   -....--..        -             =++*%%%#+++        :-     ..   .                    -  .- =      :   ')
print('                    ....=-.         -            =-.-%%%%**##        .:.     .  ::::      -        :  :  -  =          ')
print('                 - .....-..       ..-...          ...-%%=.=+*         ::.    ::   =+*= .*%*%%      =  : :- ==          ')
print('               -      .-.      ..  .--...  :            ..:-        . =  -    := .   .#*+   %%%   ::  :::  -      -    ')
print('                            -   .   --.....         ##*.-=                   : :       +++.   %%  =   ::= -- .         ')
print('               . .:        -   .=. ..-:...                                    +. *###%%+++=    %% .: ::: =-= :   -     ')
print('                :      :  -   --- ...=-...     .  .                             ===+%%%%+++    ##  =::: --- -    .     ')
print('               . -    -  -- -----.   .--..                                      ...%%%%+*##    ##  ::: --- -     =-    ')
print('             .....   -  -- -=----    ..-:.                                      -. .+-..=+=    ** +::+==+--  :   .     ')
print('            . .-. .. - =- -------=     .-    .                       *                ..=     *+# : =+---   .          ')
print('           .:-..--..-..---=-=-----     --                                          .          +    . =      .          ')
print('           . --. =..-.-----+-------    --   -                                                     = ::-  ..      =     ')
print('                  ..-.=-:----------   ----                                                        :::::  .             ')
print('                  ..-.- -=++ =-----= --- -              #*======+                   .         ...::::  ...      -      ')
print('                   .=-  =-+   -----------  -            ::::::::=====                 .      ...::::  .....     .      ')
print('                    .-  =-    =+--------                :::::::::::===*                    ....:+:   .....:    =       ')
print('                     =-  -:    =+-=.==-...-=-           +:::::::::---=**                -...:..   ........-            ')
print('                          -   -=    ==...===..           :::::--::-:::+          .:=:....:  ..+==.........-   .        ')
print('                             +    =-.. . + =.:-           +:::-:---::                    :  .===..........:  .         ')
print('                                 ..  .    :.::::             .:::-                      -==..===.....-......-          ')
print('                                 .       .::::::::                                    -===..===.-........-.            ')
print('#######                                  ::::::::::-                                ---==-.=====....=.:..=.            ')
print('####:    :.                            ::::::::::::::-                          .========..====....=-....=.-           ')
print('#####               =.              :::::::::::::::::::                   -==============.=====:..-=:: ::=::           ')
print('#####                             ::::::::::::::::::::::-     +-###  ===+===============+:====:::==::. .:=::           ')
print('#####+                             ::::::::::::::::::::::::::::::      ======+ =========:+====-:==::    ==::           ')
print('######                         :    ::::--::::::-::------::---::       =      :=*===- ==:== ====:+       =::           ')
print('#######                              ::-----------------------+                :     += -   ==           ::            ')
print('########.                             --------------------------                     -      +=         =:-             ')
print('\n')

def process_file(input_file):
    with open(input_file, 'r') as file:
        for line in file:
            if not (line.startswith('HEADER') or line.startswith('REMARK') or
                    line.startswith('TER') or line.startswith('END')):
                yield [float(coord) for coord in line.split()[6:9]]


def calculate_coordinates(coordinates):
    x_values, y_values, z_values = zip(*coordinates)
    x_max, y_max, z_max = max(x_values), max(y_values), max(z_values)
    x_min, y_min, z_min = min(x_values), min(y_values), min(z_values)
    x_coord, y_coord, z_coord = x_max - x_min, y_max - y_min, z_max - z_min
    return x_max, y_max, z_max, x_min, y_min, z_min, x_coord, y_coord, z_coord

def main():
    coordinates = process_file(args.input)
    x_max, y_max, z_max, x_min, y_min, z_min, x_coord, y_coord, z_coord = calculate_coordinates(coordinates)
    print([x_coord, y_coord, z_coord])
    print(x_max, y_max, z_max, x_min, y_min, z_min)

    with open(args.output, "w+") as f:
        f.write(str([x_coord, y_coord, z_coord]))

if __name__ == "__main__":
    main()