/* Установка дефолтных значений в FormControlSelect2 и FormControlSelect3 */
let dubbingSelectValue = document.getElementById('FormControlSelect1').value;
let dubbingData = document.getElementById('dubbing_studio_for_title');
let playerForDubbingStudio = dubbingData.querySelector('[data-studio-id="'+dubbingSelectValue+'"]').children;

for (let node of playerForDubbingStudio){
    let newOption = new Option(node.getAttribute('data-player-title'), node.getAttribute('data-player-id'));
    document.getElementById('FormControlSelect2').add(newOption, undefined);
};
let playerSelectValue = document.getElementById('FormControlSelect2').value;
let iframes = document.getElementById('iframes_for_player').children;

for (let node of iframes){
    if (node.getAttribute('data-iframe-dubbing-id') == dubbingSelectValue) {
        if (node.getAttribute('data-iframe-player-id') == playerSelectValue) {
            let newOption = new Option(node.getAttribute('data-iframe-number-of-episodes'), node.getAttribute('data-iframe-id'));
            document.getElementById('FormControlSelect3').add(newOption, undefined);
        }
    }
}

let episodesSelectIframeId = document.getElementById('FormControlSelect3').value;
for (let node of iframes){
    if (node.getAttribute('data-iframe-id') == episodesSelectIframeId) {
        var clonedNode = node.cloneNode(true);
        document.getElementById('iframeBoxForVideo').appendChild(clonedNode);
    }
}

document.getElementById('FormControlSelect1').addEventListener("change", function() {
    document.getElementById('FormControlSelect2').innerHTML = "";
    document.getElementById('FormControlSelect3').innerHTML = "";
    document.getElementById('iframeBoxForVideo').innerHTML = "";

    let dubbingSelectValue = document.getElementById('FormControlSelect1').value;
    let dubbingData = document.getElementById('dubbing_studio_for_title');
    let playerForDubbingStudio = dubbingData.querySelector('[data-studio-id="'+dubbingSelectValue+'"]').children;

    for (let node of playerForDubbingStudio){
        let newOption = new Option(node.getAttribute('data-player-title'), node.getAttribute('data-player-id'));
        document.getElementById('FormControlSelect2').add(newOption, undefined);
    };
    let playerSelectValue = document.getElementById('FormControlSelect2').value;
    let iframes = document.getElementById('iframes_for_player').children;

    for (let node of iframes){
        if (node.getAttribute('data-iframe-dubbing-id') == dubbingSelectValue) {
            if (node.getAttribute('data-iframe-player-id') == playerSelectValue) {
                let newOption = new Option(node.getAttribute('data-iframe-number-of-episodes'), node.getAttribute('data-iframe-id'));
                document.getElementById('FormControlSelect3').add(newOption, undefined);
            }
        }
    }
    let episodesSelectIframeId = document.getElementById('FormControlSelect3').value;
    for (let node of iframes){
        if (node.getAttribute('data-iframe-id') == episodesSelectIframeId) {
            var clonedNode = node.cloneNode(true);
            document.getElementById('iframeBoxForVideo').appendChild(clonedNode);
        }
    }
});

document.getElementById('FormControlSelect2').addEventListener("change", function() {
    document.getElementById('FormControlSelect3').innerHTML = "";
    document.getElementById('iframeBoxForVideo').innerHTML = "";
    let dubbingSelectValue = document.getElementById('FormControlSelect1').value;
    let playerSelectValue = document.getElementById('FormControlSelect2').value;
    let iframes = document.getElementById('iframes_for_player').children;

    for (let node of iframes){
        if (node.getAttribute('data-iframe-dubbing-id') == dubbingSelectValue) {
            if (node.getAttribute('data-iframe-player-id') == playerSelectValue) {
                let newOption = new Option(node.getAttribute('data-iframe-number-of-episodes'), node.getAttribute('data-iframe-id'));
                document.getElementById('FormControlSelect3').add(newOption, undefined);
            }
        }
    }
    let episodesSelectIframeId = document.getElementById('FormControlSelect3').value;
    for (let node of iframes){
        if (node.getAttribute('data-iframe-id') == episodesSelectIframeId) {
            var clonedNode = node.cloneNode(true);
            document.getElementById('iframeBoxForVideo').appendChild(clonedNode);
        }
    }
});

document.getElementById('FormControlSelect3').addEventListener("change", function() {
    document.getElementById('iframeBoxForVideo').innerHTML = "";

    let iframes = document.getElementById('iframes_for_player').children;
    let episodesSelectIframeId = document.getElementById('FormControlSelect3').value;
    for (let node of iframes){
        if (node.getAttribute('data-iframe-id') == episodesSelectIframeId) {
            var clonedNode = node.cloneNode(true);
            document.getElementById('iframeBoxForVideo').appendChild(clonedNode);
        }
    }
});