import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { HttpErrorResponse, HttpResponse } from '@angular/common/http';

import { Observable, throwError } from 'rxjs';
import { catchError, retry } from 'rxjs/operators';
import { TEAM } from '../mock-team';
import { Team } from '../team'


@Injectable({
  providedIn: 'root',
})
export class ApiDataService {
  baseUrl = 'http://localhost:5000/';
  teamListApi = 'api/nba/team/list'

  constructor(private http: HttpClient) { }

  getTeamList(): Observable<Team[]> { 
    let url = this.baseUrl + this.teamListApi
    return this.http.get<Team[]>(url).pipe(
      catchError(this.handleError)
    );
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

