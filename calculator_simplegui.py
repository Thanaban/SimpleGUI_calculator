import PySimpleGUI as sg
sg.ChangeLookAndFeel('Dark')
answer2 =''

layout = [
          [sg.Text('', size=(10, 1), font=('Helvetica', 30), text_color='green', key='input')],
        #[sg.Input(size=(31, 10), do_not_clear=True, justification='right', key='input')],
          [sg.Text('', size=(10, 1), font=('Helvetica', 30), text_color='green', key='out')],
          [sg.ReadFormButton('+',button_color=('blue', '#fff8b7')), sg.ReadFormButton('-',button_color=('blue', '#fff8b7')), sg.ReadFormButton('*',button_color=('blue', '#fff8b7')),sg.ReadFormButton('/',button_color=('blue', '#fff8b7'))],
          [sg.ReadFormButton('7',button_color=('blue', '#fff8b7')), sg.ReadFormButton('8',button_color=('blue', '#fff8b7')), sg.ReadFormButton('9',button_color=('blue', '#fff8b7')),sg.ReadFormButton('AC',button_color=('blue', '#fff8b7'))],
          [sg.ReadFormButton('4',button_color=('blue', '#fff8b7')), sg.ReadFormButton('5',button_color=('blue', '#fff8b7')), sg.ReadFormButton('6',button_color=('blue', '#fff8b7')),sg.ReadFormButton('DEL',button_color=('blue', '#fff8b7'))],
          [sg.ReadFormButton('1',button_color=('blue', '#fff8b7')), sg.ReadFormButton('2',button_color=('blue', '#fff8b7')), sg.ReadFormButton('3',button_color=('blue', '#fff8b7')),sg.ReadFormButton('ANS',button_color=('blue', '#fff8b7'))],
          [sg.ReadFormButton('.',button_color=('blue', '#fff8b7')),sg.ReadFormButton('0',button_color=('blue', '#fff8b7')),sg.ReadFormButton('(',button_color=('blue', '#fff8b7')),sg.ReadFormButton(')',button_color=('blue', '#fff8b7'))],
          [sg.ReadFormButton('=',button_color=('blue', '#fff8b7'))]
          ]

form = sg.FlexForm('calculator', default_button_element_size=(8,2), auto_size_buttons=False, grab_anywhere=False)
form.Layout(layout)
OP =  ['+','-','*','/','(','.']
# Loop forever reading the form's values, updating the Input field
Input1 = ''
while True:
    #num = ['1','2','3','4','5','6','7','8','9','+','-','*','/']
    #answer2 = ''
    button, values = form.Read()  # read the form
    if len(str(Input1)) < 10:
        if button is None:  # if the X button clicked, just exit
            break
        elif button is 'AC':  # clear keys if clear button
            Input1 = ''
            form.FindElement('input').Update(Input1)
            form.FindElement('out').Update(answer2)
        elif button is 'DEL':
            Input1 = Input1[:-1]
            form.FindElement('input').Update(Input1)
            form.FindElement('out').Update(answer2)
        elif button is 'ANS':
            Input1 = Input1 + str(answer2)
            form.FindElement('input').Update(Input1)
            answer2 =''
            form.FindElement('out').Update(answer2)
        elif button is '.':
            if Input1=='':
                Input1 = Input1 + '0.'
            else:
                Input1 = Input1 + '.'
                form.FindElement('input').Update(Input1)
                form.FindElement('out').Update(answer2)  
        elif button in '1234567890+-*/()':
            Input1 += button  # add the new digit
            form.FindElement('input').Update(Input1)
            form.FindElement('out').Update(answer2)  
        elif button is '=':
            for i in OP:
                if '.' is Input1[0] or '/' is Input1[0] or '*' is Input1[0] or i is Input1[-1] or ')' is Input1[0]:
                    Input1 = ''
                    answer2 ='ERROR'
                    form.FindElement('input').Update(Input1)
                    form.FindElement('out').Update(answer2)
                    break
                elif '++' in Input1 or '+-' in Input1 or '+/' in Input1 or '+*' in Input1 or '+.' in Input1:
                    Input1 = ''
                    answer2 ='ERROR'
                    form.FindElement('input').Update(Input1)
                    form.FindElement('out').Update(answer2)
                    break
                elif '-+' in Input1 or '--' in Input1 or '-*' in Input1 or '-/' in Input1 or '-.' in Input1:
                    Input1 = ''
                    answer2 ='ERROR'
                    form.FindElement('input').Update(Input1)
                    form.FindElement('out').Update(answer2)
                    break
                elif '*+' in Input1 or '*-' in Input1 or '*/' in Input1 or '*.'in Input1:
                    Input1 = ''
                    answer2 ='ERROR'
                    form.FindElement('input').Update(Input1)
                    form.FindElement('out').Update(answer2)
                    break
                elif '/+' in Input1 or '/-' in Input1 or '/*' in Input1 or '//' in Input1 or '/.' in Input1:
                    Input1 = ''
                    answer2 ='ERROR'
                    form.FindElement('input').Update(Input1)
                    form.FindElement('out').Update(answer2)
                    break
                elif '(' in Input1:
                    if ')' not in Input1:
                        Input1 = ''
                        answer2 ='ERROR'
                        form.FindElement('input').Update(Input1)
                        form.FindElement('out').Update(answer2)
                        break   
                elif '(' not in Input1:
                    if ')' in Input1:
                        Input1 = ''
                        answer2 ='ERROR'
                        form.FindElement('input').Update(Input1)
                        form.FindElement('out').Update(answer2)
                        break   
                
        #if Input1[0]='*' and Input1[0]='/' and Input1[0]='+':
            #answer2 = 'ERROR'
            else:
                answer2 =eval(Input1)
                Input1 = ''
                form.FindElement('input').Update(Input1)
                form.FindElement('out').Update(answer2)
    else:
        Input1 = 'PRESS_AC_' 
        form.FindElement('input').Update(Input1)
        form.FindElement('out').Update(answer2)
    #form.FindElement('input').Update(Input1)
    #form.FindElement('out').Update(answer2)  # output the final string
        

        