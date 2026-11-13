# AION WORK: odczyt poczty i kalendarza z klasycznego Outlooka na Windows. Tylko odczyt.
# Nagłówki:  powershell -NoProfile -ExecutionPolicy Bypass -File poczta-outlook.ps1 [-Godziny 24] [-Limit 50]
# Treść:     powershell -NoProfile -ExecutionPolicy Bypass -File poczta-outlook.ps1 -Tresc <id wiadomości>
# Nowy Outlook dla Windows nie udostępnia skrzynki skryptom; potrzebny jest klasyczny Outlook.
param([int]$Godziny = 24, [int]$Limit = 50, [string]$Tresc = "")

[Console]::OutputEncoding = [System.Text.Encoding]::UTF8
try {
    $outlook = New-Object -ComObject Outlook.Application
    $ns = $outlook.GetNamespace("MAPI")
} catch {
    Write-Output "BŁĄD: nie ma klasycznego Outlooka albo nie można go otworzyć. Nowy Outlook dla Windows nie udostępnia poczty skryptom."
    exit 1
}

if ($Tresc -ne "") {
    try {
        $m = $ns.GetItemFromID($Tresc)
        Write-Output ("OD: {0} <{1}>" -f $m.SenderName, $m.SenderEmailAddress)
        Write-Output ("TEMAT: {0}" -f $m.Subject)
        Write-Output ("DATA: {0:yyyy-MM-dd HH:mm}" -f $m.ReceivedTime)
        Write-Output ""
        Write-Output $m.Body
    } catch {
        Write-Output "BŁĄD: nie znalazłem wiadomości $Tresc."
    }
    exit 0
}

function Format-Data($d) { return $d.ToString("g") }

Write-Output "KALENDARZ (dziś i jutro)"
try {
    $dzis = (Get-Date).Date
    $koniec = $dzis.AddDays(2)
    $kal = $ns.GetDefaultFolder(9).Items
    $kal.IncludeRecurrences = $true
    $kal.Sort("[Start]")
    $filtr = "[Start] >= '" + (Format-Data $dzis) + "' AND [Start] < '" + (Format-Data $koniec) + "'"
    foreach ($z in $kal.Restrict($filtr)) {
        Write-Output ("{0:yyyy-MM-dd HH:mm} | {1} | {2}" -f $z.Start, $z.Subject, $z.Location)
    }
} catch {
    Write-Output ("BŁĄD KALENDARZA: " + $_.Exception.Message)
}

Write-Output ""
Write-Output "POCZTA (ostatnie $Godziny h): czas | nadawca | temat | status | id"
try {
    $od = (Get-Date).AddHours(-$Godziny)
    $skrzynka = $ns.GetDefaultFolder(6).Items
    $skrzynka.Sort("[ReceivedTime]", $true)
    $n = 0
    foreach ($m in $skrzynka.Restrict("[ReceivedTime] >= '" + (Format-Data $od) + "'")) {
        if ($m.Class -ne 43) { continue }
        $status = if ($m.UnRead) { "nieprzeczytany" } else { "przeczytany" }
        Write-Output ("{0:yyyy-MM-dd HH:mm} | {1} <{2}> | {3} | {4} | {5}" -f $m.ReceivedTime, $m.SenderName, $m.SenderEmailAddress, $m.Subject, $status, $m.EntryID)
        $n++
        if ($n -ge $Limit) { break }
    }
    if ($n -eq 0) { Write-Output "Brak nowych wiadomości w skrzynce odbiorczej Outlooka." }
} catch {
    Write-Output ("BŁĄD POCZTY: " + $_.Exception.Message)
}
