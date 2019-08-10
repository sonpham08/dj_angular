import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { HttpHeaders } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class ApiService {
  csrftoken = this.getCookie('csrftoken');
  getCookie(name) {
      var cookieValue = null;
      if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
          var cookie = cookies[i].trim();
          if (cookie.substring(0, name.length + 1) === (name + '=')) {
            cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
            break;
          }
        }
      }
      return cookieValue;
  }

  baseUrl : string = "http://localhost:8000/api/";
  httpHeaders = new HttpHeaders({
    'Content-type': 'application/json',
  });

  constructor(
    private http: HttpClient
  ) { }

  getAllProduct(): Observable<any> {
    return this.http.get(this.baseUrl + 'products/', {headers: this.httpHeaders});
  }

  login(data): Observable<any> {
    return this.http.post('http://localhost:8000/rest-auth/login/', data, {headers: this.httpHeaders});
  }

  getCurrentUser(): Observable<any> {
    let token = localStorage.getItem('token');
    let headers = new HttpHeaders({
      'Content-type': 'application/json',
      'Authorization': `Token ${token}`
    })
    return this.http.get(this.baseUrl + 'users/me/', { headers: headers });
  }
}
