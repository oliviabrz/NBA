import { Component, OnInit, AfterViewInit, ViewChild } from '@angular/core';
import { GameStats } from '../game-stats';
import { GAMESTATS } from '../mock-game-stats';
import { ApiDataService } from '../apiData/api.data.service';
@Component({
  selector: 'app-game-stats',
  templateUrl: './game-stats.component.html',
  styleUrls: ['./game-stats.component.scss']
})
export class GameStatsComponent implements OnInit, AfterViewInit {

  gameStats: GameStats[] = new Array<GameStats>();
  
  constructor(private apiDataService: ApiDataService) { }

  ngOnInit(): void {
    // this is api data:
    this.apiDataService.getGameStats()
    .subscribe((data) => {    
      this.gameStats = data.map<GameStats>(obj => {
        return <GameStats>
        {
          Ast : parseFloat(obj.Ast),
          Blk : parseFloat(obj.Blk),
          Dreb : parseFloat(obj.Dreb),
          Fg3Pct : parseFloat(obj.Fg3Pct),
          Fg3a : parseFloat(obj.Fg3a),
          Fg3m : parseFloat(obj.Fg3m),
          FgPct: parseFloat(obj.FgPct),
          Fga : parseFloat(obj.Fga),
          Fgm : parseFloat(obj.Fgm),
          FtPct : parseFloat(obj.FtPct),
          Fta : parseFloat(obj.Fta),
          Ftm : parseFloat(obj.Ftm),
          Min : parseFloat(obj.Min),
          Oreb : parseFloat(obj.Oreb),
          Pf : parseFloat(obj.Pf),
          Pts : parseFloat(obj.Pts),
          Reb : parseFloat(obj.Reb),
          Stl : parseFloat(obj.Stl),
          Turnover : parseFloat(obj.Turnover)
        } 
    });
    });
  }

  ngAfterViewInit() {
  }
}
