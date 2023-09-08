const puppeteer = require('puppeteer');
const sleep = require('await-sleep');
const fs = require('fs');

(async () => {
    const browser = await puppeteer.launch();
    const page = await browser.newPage();

  

    function extractProducts() {
        const data = [];
        var products = document.querySelectorAll('.ais-InfiniteHits-item');
        for (var product of products) {
            data.push({
                Url: product.querySelector('a').getAttribute("href"),
                About: product.querySelector('a').innerText
            });
        }
        return data;
    }
    
    async function paginateAndScrape() {
        const result = [];
        for(var p = 99; p <= 100; p++){

          await page.goto('https://www.coursera.org/search?query=SPECIALIZATION&page=100&index=prod_all_launched_products_term_optimization', {
            waitUntil: 'networkidle0',
          });

          let products = await page.evaluate(extractProducts);
          console.log(`Found ${products.length} products on page ${p}`);
      
          result.push(...products);
          console.log(result);

        }
        return result;
    }
    
    console.log('Navigating...');


    const result  = await paginateAndScrape();
    

        
    fs.writeFile("output.json", JSON.stringify(result), 'utf8', function (err) {
        if (err) {
            console.log("An error occured while writing JSON Object to File.");
            return console.log(err);
        }
     
        console.log("JSON file has been saved.");
        browser.close();
    });
    //console.log(JSON.stringify(result));


  })();


   


