import { Injectable } from '@angular/core';

import { Resolve, ActivatedRouteSnapshot, RouterStateSnapshot } from "@angular/router";
import { Observable, timer } from "rxjs";

import { HttpClient } from '@angular/common/http';

import { ApiService } from "./api.service";

@Injectable({
    providedIn: 'root'
})
export class GlobalResolverService implements Resolve<any> {
    private websiteBaseUrl: string;
    private credentials: any;

    constructor(
        private http: HttpClient,
        private apiService: ApiService,
    ) { 
    }

    resolve(route: ActivatedRouteSnapshot, routerState: RouterStateSnapshot): Observable<any> {
        this.reportVisit(routerState);
        return timer(160);
    }

    reportVisit(routerState) {
        if (!this.apiService.isLocalDev()){
            // TODO: not safe to grant api key to client side
            let param: any = {
                'query': 'get_api_key',
            };
            // console.log('getting api key');
            this.http.get<any>(`${this.apiService.getBaseUrl()}report`, { params: param }).subscribe(
                response => {
                    // console.log('getting api key successful, server responded with', response);
                    this.credentials = response.data;
                    param = {
                        'access_key': this.credentials,
                        'fields': 'city, region_name, country_name, zip, ip, hostname, type, continent_name, latitude, longitude',
                    };
                    // console.log('reporting to server');
                    this.http.get<any>(`//api.ipstack.com/check`, { params: param }).subscribe(
                        response => {
                            // console.log('got api key from server!', response);
                            let param = response;
                            param['visitingPath'] = routerState.url;
                            param.query = "report_visit";
                            this.http.get<any>(`${this.apiService.getBaseUrl()}report`, { params: param }).subscribe(
                                response => {
                                    // console.log("successfully reported. server responded with", response);
                                }
                            );
                        },
                        error => {

                        }
                    );
                },
                error => {
                    // console.error("fail to get api key from server");
                }
            );
        } 
        else {
            // console.log("local dev detected: will not report visitor.");
        }
    }
}