import { Injectable } from '@angular/core';

import { HttpClient, HttpHeaders } from '@angular/common/http';

import { timeout } from 'rxjs/operators';

@Injectable({
    providedIn: 'root'
})
export class ApiService {

    // http options used for making API calls
    private httpOptions: any;

    private DEBUG: boolean = false;

    constructor(
        private http: HttpClient,
    ) {
        this.httpOptions = {
            headers: new HttpHeaders({
                'Content-Type': 'application/json',
            })
        };
    }

    public getApiBaseUrl() {
        if (window.location.hostname === 'localhost') {
            return `//localhost:8001/api/`;
        } else {
            return '/api/';
        }
    }

    public getBaseUrl() {
        if (window.location.hostname === 'localhost') {
            return `//localhost:8001/`;
        } else {
            return '/';
        }
    }

    public isLocalDev() {
        if (this.getBaseUrl() == `/`) {
            return false;
        } else {
            return true;
        }
    }
    

    /** 
     * 
     * RESTful API 
     * 
     */

    public apiGetEndPoint(path, params?, token?, absolutePath?, relativePath?) {
        let queryUrl = (absolutePath) ? absolutePath : `${this.getApiBaseUrl()}${path}/`;
        if (relativePath) queryUrl = `${this.getBaseUrl()}${relativePath}/`;

        if (this.DEBUG && this.isLocalDev()) console.log('GET:', queryUrl, token, params);
        return this.http.get(queryUrl, {
            headers: new HttpHeaders({
                'Content-Type': 'application/json',
                'Authorization': (token) ? 'JWT ' + token : '',
            }),
            params: (params) ? params : {},
        })
        .pipe(
            timeout(10000),
        );
        // object service (CRUD layer) handles error
    }

    public apiPostEndPoint(path, data?, token?, absolutePath?) {
        let queryUrl = (absolutePath) ? absolutePath : `${this.getApiBaseUrl()}${path}/`;
        let formData = (data) ? JSON.stringify(data) : {};
        let httpOptions = Object.assign({
            headers: new HttpHeaders({
                'Content-Type': 'application/json',
                'Authorization': (token) ? 'JWT ' + token : '',
            })
        });
        if (this.DEBUG) console.log('POST:', queryUrl, token, formData, httpOptions);
        return this.http.post(queryUrl,
            formData,
            httpOptions,
        );
    }

    public apiPutEndPoint(path, data?, token?, absolutePath?) {
        let queryUrl = (absolutePath) ? absolutePath : `${this.getApiBaseUrl()}${path}/`;
        let formData = (data) ? JSON.stringify(data) : {};
        let httpOptions = Object.assign({
            headers: new HttpHeaders({
                'Content-Type': 'application/json',
                'Authorization': (token) ? 'JWT ' + token : '',
            })
        });
        if (this.DEBUG) console.log('PUT:', queryUrl, token, formData, httpOptions);
        return this.http.put(queryUrl,
            formData,
            httpOptions,
        );
    }

    public apiPatchEndPoint(path, data?, token?, absolutePath?) {
        let queryUrl = (absolutePath) ? absolutePath : `${this.getApiBaseUrl()}${path}/`;
        let httpOptions = {
            headers: new HttpHeaders({
                'Content-Type': 'application/json',
                'Authorization': (token) ? 'JWT ' + token : '',
            })
        };
        if (this.DEBUG) console.log('PATCH:', queryUrl, token, data, httpOptions);
        return this.http.patch(queryUrl,
            (data) ? JSON.stringify(data) : {},
            httpOptions,
        );
    }

    public apiDeleteEndPoint(path, token?, absolutePath?) {
        let queryUrl = (absolutePath) ? absolutePath : `${this.getApiBaseUrl()}${path}/`;
        let httpOptions = {
            headers: new HttpHeaders({
                'Content-Type': 'application/json',
                'Authorization': (token) ? 'JWT ' + token : '',
            })
        };
        if (this.DEBUG) console.log('DELETE:', queryUrl, token, httpOptions);
        return this.http.delete(queryUrl,
            httpOptions,
        );
    }

    public apiPostFileEndPoint(path, formData, token) {
        let queryUrl = `${this.getApiBaseUrl()}${path}/`;
        let httpOptions = {
            headers: new HttpHeaders({
                'Authorization': (token) ? 'JWT ' + token : '',
            })
        };
        if (this.DEBUG) console.log('POST FILE:', queryUrl, token, httpOptions);        
        return this.http.post(queryUrl,
            formData,
            httpOptions,
        );
    }

    /** 
     * 
     * Helpers 
     * 
     */
}
