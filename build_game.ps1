
# Auto-sync generator script: Re-runs generate_perfect_game.py to keep HTML 100% clean
python "$PSScriptRoot\generate_perfect_game.py"
Write-Host "NexEdu_ChildrensDay_Games.html built & verified successfully!"
