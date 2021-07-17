import { Component, OnInit, AfterViewInit, ViewChild } from '@angular/core';
import { GameStats } from '../game-stats';
import { GAMESTATS } from '../mock-game-stats';
import { ApiDataService } from '../apiData/api.data.service';
import { MatTableDataSource } from '@angular/material/table';
import { Kvp } from '../kvp';
import { MatPaginator } from '@angular/material/paginator';

@Component({
  selector: 'app-game-stats',
  templateUrl: './game-stats.component.html',
  styleUrls: ['./game-stats.component.scss']
})
export class GameStatsComponent implements OnInit, AfterViewInit {

  @ViewChild(MatPaginator) paginator!: MatPaginator;
  gameStats: GameStats[] = new Array<GameStats>();
  dsTable: MatTableDataSource<GameStats>;
  displayedColumns  :  string[] = ['id', 'fullName'] //'name', 'abbreviation', 'city', 'conference', 'division'];
  
  constructor(private apiDataService: ApiDataService) { 
    this.dsTable = new MatTableDataSource<GameStats>();
    //console.info('In constructor')
  }

  ngOnInit(): void {
    // this is api data:
    this.apiDataService.getGameStats()
    .subscribe((data) => {    
    this.dsTable.data = data
    });
  }
  
  ngAfterViewInit() {
    this.dsTable.paginator = this.paginator;
  }
}
