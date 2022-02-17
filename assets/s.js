var settings = {
    "url": "https://fierce-springs-06377.herokuapp.com/",
    "method": "POST",
    "timeout": 0,
    "headers": {
      "Content-Type": "application/json"
    },
  };
$(".submitB").on("click", function(e){
    e.preventDefault();    
    let hisName = $("input[name='hisname']")[0].value;
    let herName = $("input[name='hername']")[0].value;
    request=JSON.parse(JSON.stringify(settings))
    data ={       
        "mname": hisName,
        "fname": herName
    }
    request["data"]=JSON.stringify(data);
    console.log(request.url)
    $.ajax(request).done(function (response) {
        console.log(response);
        $(".responsePercentage")[0].innerHTML=response.percentage+"% love"
        $("#hide")[0].classList=["show"]
        $(".responseText")[0].innerHTML=response.result
    });
})
