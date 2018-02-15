function buildPlot() {
    /* data route */
    var url = "/api/data";
    Plotly.d3.json(url, function (error, response) {

        console.log(response);

        var data = response

        var data = [{
            x: response,
            y: Plotly.d3.range(0, response.length),
            type: 'bar'
        }];

        Plotly.newPlot('plot', data);

    });
}

buildPlot();
