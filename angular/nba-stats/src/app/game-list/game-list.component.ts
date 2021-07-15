import { Component, OnInit, AfterViewInit, ViewChild } from '@angular/core';
import { Game } from '../game';
import { GAMES } from '../mock-games';
import { ApiDataService } from '../apiData/api.data.service';
import { MatTableDataSource } from '@angular/material/table';
import { Kvp } from '../kvp';
import { MatPaginator } from '@angular/material/paginator';

@Component({
  selector: 'app-game-list',
  templateUrl: './game-list.component.html',
  styleUrls: ['./game-list.component.scss']
})

export class GameListComponent implements OnInit, AfterViewInit {
  @ViewChild(MatPaginator) paginator!: MatPaginator;
  games: Game[] = new Array<Game>();
  dsTable: MatTableDataSource<Game>;
  displayedColumns  :  string[] = ['gameDate', 'season', 'homeTeamFullName', 'homeTeamScore', 'visitorTeamFullName', 'visitorTeamScore']

  constructor(private apiDataService: ApiDataService) {
    this.dsTable = new MatTableDataSource<Game>();
    //console.info('In constructor')
   }

  ngOnInit(): void {
    // this is api data:
    this.apiDataService.getGameList()
    .subscribe((data) => {    
      this.dsTable.data = data
    });
  }

  ngAfterViewInit(): void {
    this.dsTable.paginator = this.paginator;
  }
}