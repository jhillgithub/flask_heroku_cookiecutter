function buildPlot() {
    /* data route */
    var url = "/api/data";
    Plotly.d3.json(url, function (error, response) {

        console.log(response);

        var names = response.names;
        var heights = response.heights;

        var data = [{
            x: names,
            y: heights,
            type: 'bar'
        }];

        Plotly.plot('plot', data);

    });
}

buildPlot();
