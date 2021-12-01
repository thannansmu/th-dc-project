main_template = """<style>
  html {{
      background-color:#f0f4fc;
    }}
    
    h1 {{
      text-align: center;
    }}
    
    h2 {{
      position:absolute;
      top:100px;
    }}
    
    table {{
        position:absolute;
       table-layout: fixed;
       top: 300px;
       width: 800px;
     }}

     tr, td {{
       background-color: white;
       color: back;
       border: 1px solid black;
       font-size: 20;
       text-align:center;
     }}
    
    #text-box {{
      position:absolute;
      top:175px;
    }}
    
</style>

<h1>Truth Table Maker</h1>
<h2>Enter formula:</h2>
<form id = "text-box" action="/create_table" method="post">
    <input type="text" name="formula">
    <input type="submit">
</form>


<table>
{0}
</table>
"""




