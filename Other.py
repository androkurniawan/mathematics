import PySimpleGUI as sg

def create_layout():
    layout = [
        [sg.Text('Nama Produk:'), sg.Input(key='-PRODUK-')],
        [sg.Text('Harga:'), sg.Input(key='-HARGA-')],
        [sg.Text('Jumlah:'), sg.Input(key='-JUMLAH-')],
        [sg.Button('Tambah'), sg.Button('Hitung Total'), sg.Button('Bersihkan')],
        [sg.Text('Daftar Belanja:')],
        [sg.Multiline(size=(45, 10), key='-DAFTAR-', disabled=True)],
        [sg.Text('Total: Rp'), sg.Text('0', key='-TOTAL-')]
    ]
    return layout

def run_kasir():
    window = sg.Window('Program Kasir Sederhana', create_layout())
    
    daftar_belanja = []
    total = 0

    while True:
        event, values = window.read()

        if event == sg.WINDOW_CLOSED:
            break

        if event == 'Tambah':
            try:
                produk = values['-PRODUK-']
                harga = float(values['-HARGA-'])
                jumlah = int(values['-JUMLAH-'])
                subtotal = harga * jumlah
                
                item = f"{produk} - {jumlah} x Rp{harga:.2f} = Rp{subtotal:.2f}\n"
                daftar_belanja.append(item)
                
                window['-DAFTAR-'].update(''.join(daftar_belanja))
                window['-PRODUK-'].update('')
                window['-HARGA-'].update('')
                window['-JUMLAH-'].update('')
            except ValueError:
                sg.popup_error('Masukkan harga dan jumlah yang valid!')

        if event == 'Hitung Total':
            total = sum(float(item.split('=')[1].strip()[2:]) for item in daftar_belanja)
            window['-TOTAL-'].update(f'{total:.2f}')

        if event == 'Bersihkan':
            daftar_belanja = []
            total = 0
            window['-DAFTAR-'].update('')
            window['-TOTAL-'].update('0')

    window.close()

if __name__ == '__main__':
    run_kasir()