CFG_TYPE_DATA = [
    ['prog', 'Ustawienia programów'],
    ['sync', 'Synchronizacja'],
    ['wthr', 'Ustawienia pomiaru pogody'],
    ['syst', 'Ustawienia systemowe'],
]

CFG_COMMAND_DATA = [
    ['prog', 'chk_cmd', 'Rozdzielczość wykonywania poleceń [s]', '1'],
    ['wthr', 'chk_sns', 'Rozdzielczość wykonywania pomiarów [s]', '15'],
    ['wthr', 'sv_sns', 'Rozdzielczość zapisu pomiarów [m]', '15'],
    ['wthr', 'new_sns', 'Wysłany nowy pomiar pogody', 'False'],
    ['wthr', 'week_sns', 'Zapis średnich tygodniowych', 'True'],
    ['wthr', 'long_sns', 'Zapis średnich dziennych', 'True'],
    ['sync', 'itf_nprog', 'Nowe dane programu z interfejsu', 'False'],
    ['sync', 'itf_ngpio', 'Nowe dane gpio z interfejsu', 'False'],
    ['sync', 'hdw_nprog', 'Nowe dane programu z urządzenia', 'False'],
    ['sync', 'hdw_ngpio', 'Nowe dane gpio z urządzenia', 'False'],
    ['syst', 'rb_sys', 'Restart systemu', 'False'],
    ['syst', 'pwr_off_sys', 'Wyłączenie systemu', 'False'],
    ['syst', 'updt_sys', 'Aktualizacja oprogramowania', 'False'],
]
