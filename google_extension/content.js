//content.js
	function download(filename, text)
	{
  		var element = document.createElement('a');
  		element.setAttribute('href', 'data:text/plain;charset=utf-8,' + encodeURIComponent(text));
  		element.setAttribute('download', filename);
  		element.style.display = 'none';
  		document.body.appendChild(element);
  		element.click();
  		document.body.removeChild(element);
	}

function getCurrentTabUrl() {
  var queryInfo = {
    active: true,
    currentWindow: true,
  };
	var x=function(tabs){
		var tab=tabs[0];
		var y=tab.url;
		//alert(y);
		download("googlemaps.txt",y);
		//alert("done");
	};
	
	
	chrome.tabs.query(queryInfo,x);
}

getCurrentTabUrl();
//document.querySelector('#me').addEventListener('click', getCurrentTabUrl);
