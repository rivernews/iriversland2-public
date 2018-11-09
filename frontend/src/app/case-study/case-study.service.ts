import { Injectable } from '@angular/core';

// Request Server Data
import { Observable } from 'rxjs';

// Mock data
import { HighlightedCaseStudy } from '../posts/post';

import { HttpClient } from '@angular/common/http';

import { DomSanitizer } from "@angular/platform-browser";

import { ApiService } from "../services/api.service";

@Injectable({
    providedIn: 'root'
})
export class CaseStudyService {
    private caseStudiesUrl;
    private highlightedCaseStudiesUrl;

    public caseStudies: any[];

    constructor(
        private http: HttpClient,
        public sanitizer: DomSanitizer,
        private apiService: ApiService,
    ) {
        this.highlightedCaseStudiesUrl = `${this.apiService.getApiBaseUrl()}highlighted-case-studies/`;
    }

    getHighlightedCaseStudies(): Observable<any[]> {
        return this.http.get<any[]>(this.highlightedCaseStudiesUrl);
    }


    /**
     * Sanitize Rich Text
     * 
     * DomSanitizer: https://angular.io/api/platform-browser/DomSanitizer
     * Security: https://angular.io/guide/security#xss
     * 
     */

    // TODO: better sanitize all rich text field in backend. But by default Angular will handle and strip.
    sanitizeCaseStudy(caseStudyData) {
        caseStudyData.content = this.sanitizer.bypassSecurityTrustHtml(caseStudyData.content);
        return caseStudyData;
    }
}
