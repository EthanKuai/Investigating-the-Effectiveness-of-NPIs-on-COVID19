readPage = function() {
    
    read = function(country,id1,id2,pop) {
        var i = 0;
        while ( !document.getElementsByClassName("col-md-12")[i].innerText.includes("New Cases") ) {i++;}
    	var s_cases=document.getElementsByClassName("col-md-12")[i].childNodes[5].firstChild.textContent;
    	var sTemp=s_cases.substr(s_cases.indexOf("data:"));
        var start = 0;
        while (sTemp[start]!='[') {start++;}
    	var end = start;
    	while (sTemp[end]!=']') {end++;}
    	var cases2=sTemp.substr(start,end+1);
    	var cases=eval(cases2);
    	
        i = 0;
        while ( !document.getElementsByClassName("col-md-12")[i].innerText.includes("New Deaths") ) {i++;}
    	var s_deaths=document.getElementsByClassName("col-md-12")[i].childNodes[5].firstChild.textContent;
    	var sTemp=s_deaths.substr(s_deaths.indexOf("data:"));
        start = 0;
        while (sTemp[start]!='[') {start++;}
    	var end = start;
    	while (sTemp[end]!=']') {end++;}
    	var deaths2=sTemp.substr(start,end+1);
    	var deaths=eval(deaths2);
    
        var d = new Date("15 February 2020");
        d.setDate(d.getDate() + cases.length - 1);
        var s = "";
    
        for (var i = cases.length-1; i >=0; i--) {
            if (cases[i]==null) cases[i]=0;
            if (deaths[i]==null) deaths[i]=0;
            s+=d.getDate()+'/'+(d.getMonth()+1).toString()+'/'+d.getFullYear()+','+d.getDate()+','+(d.getMonth()+1).toString()+','+d.getFullYear()+',';
            s+=cases[i].toString()+','+deaths[i].toString()+','+country+','+id1+','+id2+','+pop.toString()+',Europe\n';
            d.setDate(d.getDate() - 1);
        }
        console.log(s);
        return s;
    }

    function clipboard(text) {
    	var textArea = document.createElement("textarea");
    	textArea.style.position = 'fixed';
    	textArea.style.top = 0;
    	textArea.style.left = 0;
    	textArea.style.width = '2em';
    	textArea.style.height = '2em';
    	textArea.style.padding = 0;
    	textArea.style.border = 'none';
    	textArea.style.outline = 'none';
    	textArea.style.boxShadow = 'none';
    	textArea.style.background = 'transparent';
    	textArea.value = text;
    	document.body.appendChild(textArea);
    	textArea.focus();
    	textArea.select();
        
    	try {
    	  var successful = document.execCommand('copy');
    	} catch (err) {
    	  console.log('Oops, unable to copy');
    	}
        
    	document.body.removeChild(textArea);
    }

    var countries = ['Austria','Belgium','Denmark','France','Germany','Italy','Norway','Spain','Switzerland','United_Kingdom','uk','Greece','Netherlands','Portugal','Sweden'];
    var id1s = ['AT','BE','DK','FR','DE','IT','NO','ES','CH','UK','UK','EL','NL','PT','SE'];
    var id2s = ['AUT','BEL','DNK','FRA','DEU','ITA','NOR','ESP','CHE','GBR','GBR','GRC','NLD','PRT','SWE'];
    var pops = [8858775,11455519,5806081,67012883,83019213,60359546,5328212,46937060,8544527,66647112,66647112,10724599,17282163,10276617,10230185];

    var i = 0;
    var urlCountry = document.URL.substr(50);
    while (urlCountry!=countries[i]+'/') i++;
    if (countries[i]=='uk') i--;
    clipboard(read(countries[i],id1s[i],id2s[i],pops[i]));
}

openPages = function() {
    var countries = ['Austria','Belgium','Denmark','France','Germany','Italy','Norway','Spain','Switzerland','uk','Greece','Netherlands','Portugal','Sweden'];
    for (var i = 0; i < countries.length; i++) {
        window.open("https://www.worldometers.info/coronavirus/country/"+countries[i]+"/",'_blank');
    }
}
