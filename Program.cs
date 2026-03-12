using Microsoft.AspNetCore.Builder;
using Microsoft.AspNetCore.Http;

var builder = WebApplication.CreateBuilder(args);
var app = builder.Build();

string inputPath =  @"C:\Users\skjan\MothersonGateway\live_data.txt";;

// 1. The Web Dashboard (HTML + CSS)
string dashboardHtml = @"
<!DOCTYPE html>
<html>
<head>
    <title>Motherson Live Dashboard</title>
    <meta http-equiv='refresh' content='1'>
    <style>
        body { font-family: sans-serif; background: #1a1a1a; color: white; text-align: center; padding-top: 50px; }
        .card { background: #333; border-radius: 15px; padding: 40px; display: inline-block; box-shadow: 0 10px 30px rgba(0,0,0,0.5); }
        .count { font-size: 80px; color: #00ff00; font-weight: bold; }
        .label { font-size: 20px; color: #aaa; margin-bottom: 10px; }
    </style>
</head>
<body>
    <div class='card'>
        <div class='label'>Motherson Line 1 Production</div>
        <div class='count'>{{COUNT}}</div>
        <p>Live from Python Bridge</p>
    </div>
</body>
</html>";

// 2. Define the Web Route
app.MapGet("/", () => {
    string currentCount = "0";
    if (File.Exists(inputPath)) {
        currentCount = File.ReadAllText(inputPath).Trim();
    }
    return Results.Content(dashboardHtml.Replace("{{COUNT}}", currentCount), "text/html");
});

Console.WriteLine("--- Dashboard running at http://localhost:5005 ---");
app.Run("http://localhost:5005");