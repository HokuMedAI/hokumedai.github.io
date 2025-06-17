# Select page type
Write-Host "`nSelect page type:"
Write-Host "1. Article"
Write-Host "2. Seminar"
Write-Host "3. Mokumoku"
Write-Host "4. Meeting"
Write-Host "5. Other (default)"
$pageType = Read-Host "`nEnter number (1-5)"

# Set page type
$type = switch ($pageType) {
    "1" { "article" }
    "2" { "seminar" }
    "3" { "mokumoku" }
    "4" { "meeting" }
    "5" { "default" }
    default { 
        Write-Host "Invalid selection. Using default."
        "default"
    }
}

# Build path based on type
if ($type -eq "article") {
    Write-Host "`nEnter path for article (e.g., new_series/new_page)"
    Write-Host "Example: new_series/new_page/index.md"
    $articlePath = Read-Host "`nEnter path"
    $path = "content/articles/$articlePath/index.md"
} else {
    # Get date input for non-article types
    $today = Get-Date -Format "yyyy-MM-dd"
    $dateInput = Read-Host "`nEnter date (YYYY-MM-DD) [default: $today]"
    $date = if ($dateInput -eq "") { $today } else { $dateInput }
    $path = "content/activities/$type/$date/index.md"
}

# Execute Hugo command
Write-Host "`nWill execute the following command:"
Write-Host "hugo new $path --kind $type"
$confirm = Read-Host "`nProceed? (y/n)"

if ($confirm -eq "y") {
    # Create new page
    hugo new $path --kind $type
    
    # Update date in front matter if it's not an article
    if ($type -ne "article") {
        # Read the file content with UTF-8 encoding
        $content = Get-Content $path -Raw -Encoding UTF8
        
        # Replace the date line
        $content = $content -replace 'date: .*', "date: $date"
        
        # Write back to the file with UTF-8 encoding
        $content | Set-Content $path -NoNewline -Encoding UTF8
    }
    
    Write-Host "`nPage created: $path"
} else {
    Write-Host "`nOperation cancelled."
} 