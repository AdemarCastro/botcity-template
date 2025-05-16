$exclude = @("venv", "bot_cadastro_erp_fakturama.zip")
$files = Get-ChildItem -Path . -Exclude $exclude
Compress-Archive -Path $files -DestinationPath "bot_cadastro_erp_fakturama.zip" -Force