import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { HttpErrorResponse, HttpResponse } from '@angular/common/http';
import { of } from 'rxjs';

import { Observable, throwError } from 'rxjs';
import { catchError, retry } from 'rxjs/operators';
import { Team } from '../team';
import { Player } from '../player';
import { Game } from '../game';
import { GAMES } from '../mock-games';
//import { PLAYER } from '../mock-player';
import { PLAYERS } from '../mock-players';
//import { TEAM } from '../mock-team';
import { TEAMS } from '../mock-teams';
import { GameStats, GameStatsJson } from '../game-stats';
import { GAMESTATS } from '../mock-game-stats';


@Injectable({
  providedIn: 'root',
})
export class ApiDataService {
  baseUrl = 'http://localhost:5000/';
  playerListApi = 'api/nba/player/list';
  playerApi = 'api/nba/player';
  teamListApi = 'api/nba/team/list';
  teamApi =  'api/nba/team';
  gameListApi = 'api/nba/game/list';
  gameStatsApi = 'api/nba/game/stats/list';

  constructor(private http: HttpClient) { }

  getPlayerList(): Observable<Player[]> { 
    // return observable of mock data
    //return of(PLAYERS); 

    let url = this.baseUrl + this.playerListApi
    return this.http.get<Player[]>(url).pipe(
    catchError(this.handleError)
    );
  }

  getPlayer(first_name:string, last_name:string): Observable<Player> { 
    // return observable of mock data
    //return of(PLAYER); 

    // call api and return observable 
    let url = this.baseUrl + this.playerApi + '?first_name=' + first_name + '&last_name=' + last_name
    return this.http.get<Player>(url).pipe(
    catchError(this.handleError)
    );
  }

  getTeamList(): Observable<Team[]> { 
    //return of(TEAMS);
    
    let url = this.baseUrl + this.teamListApi
    return this.http.get<Team[]>(url).pipe(
    catchError(this.handleError)
    );
  }

  getTeam(abbreviation:string): Observable<Team> { 
    //return of(TEAM);
    
    let url = this.baseUrl + this.teamApi + '?abbreviation=' + abbreviation
    return this.http.get<Team>(url).pipe(
    catchError(this.handleError)
    );
  }

  getGameList(): Observable<Game[]> {
    //return observable of mock data
    //return of(GAMES);

    let url = this.baseUrl + this.gameListApi
    return this.http.get<Game[]>(url).pipe(
    catchError(this.handleError)
    );
  }

  getGameStats(): Observable<GameStatsJson[]> { 
    return of(GAMESTATS);
    
    // let url = this.baseUrl + this.gameStatsApi
    // return this.http.get<GameStatsJson[]>(url).pipe(
    // catchError(this.handleError)
    // );
  }

  private handleError(error: HttpErrorResponse) {
    if (error.status === 0) {
      // A client-side or network error occurred. Handle it accordingly.
      console.error('An error occurred:', error.error);
    } else {
      // The backend returned an unsuccessful response code.
      // The response body may contain clues as to what went wrong.
      console.error(
        `Backend returned code ${error.status}, ` +
        `body was: ${error.error}`);
    }
    // Return an observable with a user-facing error message.
    return throwError(
      'Something bad happened; please try again later.');
  }
}

