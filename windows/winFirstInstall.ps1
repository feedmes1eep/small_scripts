$softwares = (
    'GIMP.GIMP', 
    'Famatech.AdvancedIPScanner',
    'MEGASync',
    'EpicGames.EpicGamesLauncher',
    'Python.Python.3',
    'JetBrain.Pycharm.Community',
    'RARLab.WinRar',
    'CrystalDewWorld.CrystalDiskMark',
    'CrystalDewWorld.CrystalDiskInfo',
    'Nvidia.GeForceExperience',
    'Microsoft.VisualStudioCode',
    'Microsoft.dotnet',
    'qbittorent.qbittorent',
    'Vavle.Steam',
    'erengy.Taiga',
    'HakuNeko.HakuNeko',
    'Discord.Discord',
    'ShareX.ShareX',
    'TimKosse.FilZillaServer',
    'Git.Git',
    'GitHub.GitHubDesktop',
    'Mozilla.FireFox',
    'Mozilla.Thunderbird',
    'Rainmeter.Rainmeter.Beta',
    'ProtonTechnologies.ProtonVPN'
    )

foreach ($software in $softwares) {
    winget install $software
}

#Ill make this multithreaded later