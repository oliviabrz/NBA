import { Component, OnInit, ChangeDetectorRef, ChangeDetectionStrategy } from '@angular/core';
import { GameStats } from '../game-stats';
import { GAMESTATS } from '../mock-game-stats';
import { ApiDataService } from '../apiData/api.data.service';
import { BehaviorSubject, Observable } from 'rxjs';
import { EChartsOption } from 'echarts';
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

  gameStats: GameStats[] = new Array<GameStats>();
  array$ = new BehaviorSubject<GameStats[]>([]);//Declare your array
  echartsInstance: any;
  
  chartOption: EChartsOption = {
    xAxis: {
      type: 'category',
      data: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],
    },
    yAxis: {
      type: 'value',
    },
    series: [
      {
        data: [820, 932, 901, 934, 1290, 1330, 1320],
        type: 'line',
      },
    ],
  };

  constructor(private apiDataService: ApiDataService, 
              private changeDetection: ChangeDetectorRef) { }

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
      this.gameStats = data.map<GameStats>(obj => {
        return <GameStats>
          {
            Ast: parseFloat(obj.Ast),
            Blk: parseFloat(obj.Blk),
            Dreb: parseFloat(obj.Dreb),
            Fg3Pct: parseFloat(obj.Fg3Pct),
            Fg3a: parseFloat(obj.Fg3a),
            Fg3m: parseFloat(obj.Fg3m),
            FgPct: parseFloat(obj.FgPct),
            Fga: parseFloat(obj.Fga),
            Fgm: parseFloat(obj.Fgm),
            FtPct: parseFloat(obj.FtPct),
            Fta: parseFloat(obj.Fta),
            Ftm: parseFloat(obj.Ftm),
            Min: parseFloat(obj.Min),
            Oreb: parseFloat(obj.Oreb),
            Pf: parseFloat(obj.Pf),
            Pts: parseFloat(obj.Pts),
            Reb: parseFloat(obj.Reb),
            Stl: parseFloat(obj.Stl),
            Turnover: parseFloat(obj.Turnover)
          }
      });

      this.array$.next(this.gameStats);
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
