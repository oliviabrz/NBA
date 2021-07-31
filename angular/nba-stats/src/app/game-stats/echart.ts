export class ChartOptions {
    xAxis!: XAxis;
    yAxis!: YAxis;
    series!: Series;

    constructor() {
        this.xAxis = new XAxis();
        this.yAxis = new YAxis();
        this.series = new Series();
    }

    public ToObject() {
        let obj = {
            xAxis: {
                type: this.xAxis.type,
                data: this.xAxis.data,
            },
            yAxis: {
                type: this.yAxis.type,
            },
            series: [
                {
                    data: this.series.data,
                    type: this.series.type,
                },
            ],
        };

        return obj;
    }
}

export class XAxis {
    type: string = 'category';
    data: string[] = [];
}

export class YAxis {
    type: string = 'value';
}

export class Series {
    type: string = 'bar';
    data: number[] = [];
}
