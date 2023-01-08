import imgkit
import os

variables = [
    {
        "date": "24/09/2022",
        "time": "21:09"
    },{
        "date": "25/09/2022",
        "time": "11:09"
    },
]

options = {'width': 270, 'disable-smart-width': ''}
css = """
html, body{
  margin: 0px;
  padding: 0px;
  height: 1000px;
  width: 270px !important;
  font-family:'Lucida Console',monospace;
  color: black;
}
.shell{
  width: 270px !important;
  height: 100%;
  filter: blur(1px);
  -webkit-filter: blur(1px);
}
.bill{
  background: #fafafafa;
  width: 250px !important;
  padding:5px;
  border: 1px solid;
}
.center{
  text-align: center;
}
.logo img{
  width: 150px;
  height: 180px;
}
hr{
  border: 2px dashed;
}
table.t1, table.t2{
  width:100%;
}
.t1>tbody>tr td:nth-child(2){
  text-align: right;
}
"""
if not os.path.exists("out/"):
   # Create a new directory because it does not exist
   os.makedirs("out/")
for i, variable in enumerate(variables):
    variable['css']=css
    html = """
    <style>
    {css}
    </style>
    <div class="shell">
    <div class="bill">
        <div class="center logo">
        <img src="https://cdn.freebiesupply.com/logos/large/2x/bharat-petroleum-logo-png-transparent.png">
        </div>
        <div class="center">
        WELCOME TO BPCL !!<br />
        CIN No<br />
        M480106H1952G0008981<br />
        BP DHARUHERA SHAHEED<br />
        DINDAYAL FUELS V I L L . AKERABHIWADI TO NH 08<br />
        ROAD, HARYANA, DHARUHERA CASH MEMO<br />
        </div>
        <hr />
        <table class="t1">
        <tbody>
            <tr>
            <td>{date}</td>
            <td>{time}</td>
            </tr>
            <tr>
            <td>VAT TIN NO:</td>
            <td>120112121210</td>
            </tr>
            <tr>
            <td>DSM:</td>
            <td>CHAND</td>
            </tr>
            <tr>
            <td>INV#:</td>
            <td>6316</td>
            </tr>
            <tr>
            <td>BAY NOZL#:</td>
            <td>6316</td>
            </tr>
            <tr>
            <td>VEH SEG:</td>
            <td>43/67</td>
            </tr>
            <tr>
            <td>VEH#</td>
            <td>DL4CBA8744</td>
            </tr>
            <tr>
            <td>MODE:</td>
            <td>CARD</td>
            </tr>
        </tbody>
        </table>
        <hr />
        <table class="t2">
        <tbody>
            <tr>
            <td>PRODUCT:</td>
            <td>DIESEL</td>
            </tr>
            <tr>
            <td>RATE/LTR.:</td>
            <td>90.03</td>
            </tr>
            <tr>
            <td>AMOUNT(RS.):</td>
            <td>3000.00</td>
            </tr>
            <tr>
            <td>VOLUME(LTR.):</td>
            <td>33.32</td>
            </tr>
        </tbody>
        </table>
        <br />
        <br />
        <br />
        <br />
        <hr />
        <div class="center">
        SAVE FUEL YAANI <br />
        SAVE MONEY !!<br />
        THANK YOU !!<br />
        THANKS FOR FUELLING<br />
        WITH US. YOU CAN NOW<br />
        CALL US ON 1800 22<br />
        6344 (TOLL-FREE) FOR<br />
        QUERIES/COMPLAINTS ON<br />
        BPCL PETROL PUMPS, MAK<br />
        LUBRICANTS OR INOL. <br />
        PRODUCTS
        </div>

    </div>
    </div>
    """.format(**variable)
    imgkit.from_string(html, f'out/{i}.png', options=options)