# praca-inżynierska

## Konfiguracja

### Klucze API
W pliku `.env` zapisano dwa klucze API:
- `ASSEMBLYAI_API_KEY = "klucz1"`
- `OPENAI_API_KEY = "klucz2"`

### Automatyczne Tworzenie Plików
Plik `token.json` utworzy się automatycznie. Logowanie do systemu będzie możliwe tylko po zalogowaniu przez przypisane konto Gmail (twórcy oprogramowania).

### Utwórz Pliki Konfiguracyjne

#### `client_id.json`
Utwórz plik `client_id.json` z następującą zawartością:

```json
{
  "installed": {
    "client_id": "TWOJE_CLIENT_ID",
    "project_id": "TWOJE_PROJECT_ID",
    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
    "token_uri": "https://oauth2.googleapis.com/token",
    "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
    "client_secret": "TWOJE_CLIENT_SECRET",
    "redirect_uris": ["http://localhost"]
  }
}
```

#### `pracainz-key.json`
Utwórz plik pracainz-key.json z następującą zawartością:

```json
{
  "type": "service_account",
  "project_id": "TWOJE_PROJECT_ID",
  "private_key_id": "TWOJE_PRIVATE_KEY_ID",
  "private_key": "TWOJE_PRIVATE_KEY",
  "client_email": "TWOJE_CLIENT_EMAIL",
  "client_id": "TWOJE_CLIENT_ID",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "TWOJE_CLIENT_X509_CERT_URL"
}
```
