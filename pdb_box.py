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
            xyz = line[30:38].split()+line[38:46].split()+line[46:54].split()
            if (line.startswith('ATOM') or line.startswith('HETATM')):
                yield [float(coord) for coord in xyz]


def calculate_coordinates(coordinates):
    x_values, y_values, z_values = zip(*coordinates)
    x_max, y_max, z_max = max(x_values), max(y_values), max(z_values)
    x_min, y_min, z_min = min(x_values), min(y_values), min(z_values)
    x_coord, y_coord, z_coord = x_max - x_min, y_max - y_min, z_max - z_min
    return round(x_max, 3), round(y_max, 3), round(z_max, 3), round(x_min, 3), round(y_min, 3), round(z_min, 3), round(x_coord, 3), round(y_coord, 3), round(z_coord, 3)

def main():
    coordinates = process_file(args.input)
    x_max, y_max, z_max, x_min, y_min, z_min, x_coord, y_coord, z_coord = calculate_coordinates(coordinates)
    print([x_coord, y_coord, z_coord])
    print(x_max, y_max, z_max, x_min, y_min, z_min)

    with open(args.output, "w+") as f:
        f.write(str([x_coord, y_coord, z_coord]))

if __name__ == "__main__":
    main()
