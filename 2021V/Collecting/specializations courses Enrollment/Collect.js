const puppeteer = require('puppeteer');
const sleep = require('await-sleep');
const fs = require('fs');
const awaitSleep = require('await-sleep');


var obj = JSON.parse(fs.readFileSync('Courses_Url.json', 'utf8'));


(async () => {
    const browser = await puppeteer.launch();
    const page = await browser.newPage();

    

    function extractProducts() {
        const data = [];
        var products = document.querySelectorAll('._1fpiay2');

        for (var product of products) {
            data.push({
                Rating: product.innerText
            });

        }
        return data;
    }
    
    async function paginateAndScrape() {
        const result = [];

        await page.setDefaultNavigationTimeout(100000);

        for(var p =2001 ; p < 2021; p++){
          await page.goto('https://www.coursera.org'+obj[p].URL, {
            waitUntil: 'networkidle0',
          });

          try {
            await page.evaluate(() => {
                document.querySelector('ul > li > div > button').click();
              });
          }
          catch  {
            
          }

          try {
            
          let products = await page.evaluate(extractProducts);
          console.log(`Found ${products.length} products on page ${p}`);
      
          result.push(obj[p].URL,...products);
          console.log(result);
          }
          catch{

          }
        }
        return result;
    }
    
    console.log('Navigating...');


    const result  = await paginateAndScrape();
    

        
    fs.writeFile("2001-2021.json", JSON.stringify(result), 'utf8', function (err) {
        if (err) {
            console.log("An error occured while writing JSON Object to File.");
            return console.log(err);
        }
     
        console.log("JSON file has been saved.");
        browser.close();
    });
    //console.log(JSON.stringify(result));


  })();


   


