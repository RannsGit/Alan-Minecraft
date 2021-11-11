//alan js

// Use this sample to create your own voice commands

const url = '98.37.165.72';
const port = '1234';
var data = 0;

//Needed Actions

//Walk toggle
//Step
//Look
//Mine
//Jump
//Place
//Eat 
//Hotbar

intent('(walk | wok)', p => { 
    data = 'walk'
    var request_url = `http://${url}:${port}/recv?d=${data}`;
    api.axios.get(request_url).then((response) => {
        console.log(response.data, 'good response');
        if(response.data != 'good'){ p.play(response.data)}
    })
        .catch((error) => {
        console.log(error, 'bad response');
    });
});


intent('run', p => { 
    data = 'run'
    var request_url=`http://${url}:${port}/recv?d=${data}`;api.axios.get(request_url).then(e=>{console.log(e.data,"- good response")}).catch(e=>{console.log(e,"bad response")});
    
});

intent('stop walking', p => { 
    data = 'stopwalk'
    var request_url=`http://${url}:${port}/recv?d=${data}`;api.axios.get(request_url).then(e=>{console.log(e.data,"- good response")}).catch(e=>{console.log(e,"bad response")});
    
});

intent('step (forward | ahead)', p => { 
    data = 'stepW'
    var request_url=`http://${url}:${port}/recv?d=${data}`;api.axios.get(request_url).then(e=>{console.log(e.data,"- good response")}).catch(e=>{console.log(e,"bad response")});
    
});

intent('step left', p => { 
    data = 'stepA'
    var request_url=`http://${url}:${port}/recv?d=${data}`;api.axios.get(request_url).then(e=>{console.log(e.data,"- good response")}).catch(e=>{console.log(e,"bad response")});
    
});

intent('step right', p => { 
    data = 'stepD'
    var request_url=`http://${url}:${port}/recv?d=${data}`;api.axios.get(request_url).then(e=>{console.log(e.data,"- good response")}).catch(e=>{console.log(e,"bad response")});
    
});

intent('step (back | backwards | behind)', p => { 
    data = 'stepS'
    var request_url=`http://${url}:${port}/recv?d=${data}`;api.axios.get(request_url).then(e=>{console.log(e.data,"- good response")}).catch(e=>{console.log(e,"bad response")});
    
});

intent('jump', p => { 
    data = 'jump'
    var request_url=`http://${url}:${port}/recv?d=${data}`;api.axios.get(request_url).then(e=>{console.log(e.data,"- good response")}).catch(e=>{console.log(e,"bad response")});
    
});

intent('(turn | look) left $(NUMBER) degrees', p => { 
    data = `lookL${p.NUMBER.value}`
    var request_url = `http://${url}:${port}/recv?d=${data}`;
    api.axios.get(request_url).then((response) => {
        console.log(response.data, 'good response');
        if(response.data != 'good'){ p.play(response.data)} //Added in case degree given is out of range
    })
        .catch((error) => {
        console.log(error, 'bad response');
    });
});

intent('(turn | look) right $(NUMBER) degrees', p => { 
    data = `lookR${p.NUMBER.value}`
    var request_url = `http://${url}:${port}/recv?d=${data}`;
    api.axios.get(request_url).then((response) => {
        console.log(response.data, 'good response');
        if(response.data != 'good'){ p.play(response.data)} //Added in case degree given is out of range
    })
        .catch((error) => {
        console.log(error, 'bad response');
    });  
});

intent('(turn | look) left ', p => { 
    data = 'lookL90'
    var request_url=`http://${url}:${port}/recv?d=${data}`;api.axios.get(request_url).then(e=>{console.log(e.data,"- good response")}).catch(e=>{console.log(e,"bad response")});
    
});

intent('(turn | look) right ', p => { 
    data = 'lookR90'
    var request_url=`http://${url}:${port}/recv?d=${data}`;api.axios.get(request_url).then(e=>{console.log(e.data,"- good response")}).catch(e=>{console.log(e,"bad response")});
    
});

intent('(turn | look) (behind|around) ', p => { 
    data = 'lookR180'
    var request_url=`http://${url}:${port}/recv?d=${data}`;api.axios.get(request_url).then(e=>{console.log(e.data,"- good response")}).catch(e=>{console.log(e,"bad response")});
    
});

intent('stop', p => { 
    data = 'stop'
    var request_url=`http://${url}:${port}/recv?d=${data}`;api.axios.get(request_url).then(e=>{console.log(e.data,"- good response")}).catch(e=>{console.log(e,"bad response")});
    
});

walk, run, stopwalk, stepW,stepA,stepS,stepD,jump, lookR10, lookL10, stop, eat, mine10, run,

intent('eat', p => { 
    data = 'eat'
    var request_url=`http://${url}:${port}/recv?d=${data}`;api.axios.get(request_url).then(e=>{console.log(e.data,"- good response")}).catch(e=>{console.log(e,"bad response")});
    
});

intent('(mine|dig|breake) ', p => { 
    data = `mine${p.NUMBER.value}`
    var request_url = `http://${url}:${port}/recv?d=${data}`;
    api.axios.get(request_url).then((response) => {
        console.log(response.data, 'good response');
        if(response.data != 'good'){ p.play(response.data)} //Added in case number given is out of range (such as negative)
    })
        .catch((error) => {
        console.log(error, 'bad response');
    });  
});

intent('(mine|dig|break) (for|) $(NUMEBER) seconds', p => { 
    data = 'run'
    var request_url=`http://${url}:${port}/recv?d=${data}`;api.axios.get(request_url).then(e=>{console.log(e.data,"- good response")}).catch(e=>{console.log(e,"bad response")});
    
});

intent('stop (mining|digging|breaking)', p => { 
    data = 'stopmine'
    var request_url=`http://${url}:${port}/recv?d=${data}`;api.axios.get(request_url).then(e=>{console.log(e.data,"- good response")}).catch(e=>{console.log(e,"bad response")});
    
});

intent('(place|right click)', p => { 
    data = 'place'
    var request_url=`http://${url}:${port}/recv?d=${data}`;api.axios.get(request_url).then(e=>{console.log(e.data,"- good response")}).catch(e=>{console.log(e,"bad response")});
    
});

intent('(hit | left click)', p => { 
    data = 'hit'
    var request_url=`http://${url}:${port}/recv?d=${data}`;api.axios.get(request_url).then(e=>{console.log(e.data,"- good response")}).catch(e=>{console.log(e,"bad response")});
    
});

intent('(item | hotbar) $(NUMBER)', p => { 
    data = `hotbar${p.NUMBER.value}`
    var request_url = `http://${url}:${port}/recv?d=${data}`;
    api.axios.get(request_url).then((response) => {
        console.log(response.data, 'good response');
        if(response.data != 'good'){ p.play(response.data)} //Added in case number given is out of range
    })
        .catch((error) => {
        console.log(error, 'bad response');
    });
});

intent('eat', p => { 
    data = 'eat'
    var request_url=`http://${url}:${port}/recv?d=${data}`;api.axios.get(request_url).then(e=>{console.log(e.data,"- good response")}).catch(e=>{console.log(e,"bad response")});
    
});



