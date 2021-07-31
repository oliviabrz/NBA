import { Component, OnInit, ChangeDetectorRef, ChangeDetectionStrategy } from '@angular/core';
import { GameStats, GameStatsAggregate } from '../game-stats';
import { GAMESTATS } from '../mock-game-stats';
import { ApiDataService } from '../apiData/api.data.service';
import { BehaviorSubject, Observable } from 'rxjs';
import { EChartsOption } from 'echarts';
import { DatePipe } from '@angular/common';
import { ChartOptions } from './echart';
//import { ChartDataset, ChartOptions } from 'chart.js';
//import { Color, Label } from 'ng2-charts';

interface SeasonSelection {
  value: number;
  viewValue: string;
}
interface StatSelection {
  value: string;
  viewValue: string;
}
@Component({
  selector: 'app-game-stats',
  templateUrl: './game-stats.component.html',
  styleUrls: ['./game-stats.component.scss'],
  changeDetection: ChangeDetectionStrategy.Default
})
export class GameStatsComponent implements OnInit {
  selectedSeason: number = 2020;
  selectedStat: string | undefined
  //stats$: Observable<GameStats[]> | undefined;

  //gameStats: GameStats[] = new Array<GameStats>();
  statsAggregate: GameStatsAggregate[] = new Array<GameStatsAggregate>();
  array$ = new BehaviorSubject<GameStatsAggregate[]>([]);//Declare your array
  echartsInstance: any;

  chartOption: EChartsOption = {};
 
  constructor(private apiDataService: ApiDataService, 
              private changeDetection: ChangeDetectorRef, 
              public datepipe: DatePipe) { }

  seasonSelectionList: SeasonSelection[] = [
    { value: 2018, viewValue: '2018' },
    { value: 2019, viewValue: '2019' },
    { value: 2020, viewValue: '2020' }
  ];
  statSelectionList: StatSelection[] = [
    { value: "Ast", viewValue: "assist" },
    { value: "Blk", viewValue: "block" },
    { value: "Dreb", viewValue: "defensive rebound" },
    { value: "Fg3Pct", viewValue: "3 point field goal percentage" },
    { value: "Fg3a", viewValue: "3 point field goal attempt" },
    { value: "Fg3m", viewValue: "3 point field goals made" },
    { value: "FgPct", viewValue: "field goal percentage" },
    { value: "Fga", viewValue: "field goal attempt" },
    { value: "Fgm", viewValue: "field goals made" },
    { value: "FtPct", viewValue: "free throw percentage" },
    { value: "Fta", viewValue: "free throw attempt" },
    { value: "Ftm", viewValue: "free throws made" },
    { value: "Min", viewValue: "minutes played" },
    { value: "Oreb", viewValue: "offensive rebound" },
    { value: "Pf", viewValue: "personal fouls" },
    { value: "Pts", viewValue: "points" },
    { value: "Reb", viewValue: "rebounds" },
    { value: "Stl", viewValue: "steals" },
    { value: "Turnover", viewValue: "turnover" }
  ];

  onSubmit(formObj: any): void {
    if (!this.selectedStat) {
      alert('You must select a stat before submitting!');
      return;
    }

    this.apiDataService.getGameStats(this.selectedSeason, this.selectedStat)
    .subscribe((data) => {
      this.statsAggregate = data.map<GameStatsAggregate>(obj => {

        let year = Number(obj.StatDate.slice(3,7));
        let month = Number(obj.StatDate.slice(0, 2));
        console.log(`month=${month}, year=${year}`)
        return <GameStatsAggregate>
          {
            StatAvg: parseFloat(obj.StatAvg),
            StatMax: parseFloat(obj.StatMax),
            StatDate: new Date(year, month),
            StatName: obj.StatName
          }
      });

      let newChartOptions = new ChartOptions();
    
      // build x and y axis data arrays
      for (let stat of this.statsAggregate) {
        // build x-axis
        let formattedDate = this.datepipe.transform(stat.StatDate, 'MM-yyyy');
        //console.log(`StatDate=${stat.StatDate}, formattedDate=${formattedDate}`)
        newChartOptions.xAxis.data.push(formattedDate ? formattedDate : '');
      
        // build y-axis
        newChartOptions.series.data.push(stat.StatAvg);
      }

      this.chartOption = newChartOptions.ToObject() as EChartsOption;
    });
  }

  onChartInit(ec: any) {
    this.echartsInstance = ec;
    //alert('in onChartInit')
  }
  
  ngOnInit(): void { 
    //alert(`ngOnInit: ${this.gameStats.length}`)
  }

  ngAfterViewInit() {
    //alert(`ngAfterViewInit: ${this.gameStats.length}`)
  }
}


