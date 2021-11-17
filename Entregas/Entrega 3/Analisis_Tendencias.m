% Extraer las variables de los datos medidos
temp = Data_Iot(:,1);
hume = Data_Iot(:,2);
meta = Data_Iot(:,3);
mono = Data_Iot(:,4);
% Definición del vector de tiempos
time = (1:1:46)';
% Conversión a tablas
temp_s = timetable2table(temp);
hume_s = timetable2table(hume);
meta_s = timetable2table(meta);
mono_s = timetable2table(mono);
% Extraer variable de interés
var_meta = meta_s{:,2};
% Calculo de la pendiente
m = time\var_meta;

% Calculo de los valores para Y
calY = m*time;
calYY = calY(:,1)+755;

% Visualización de las tendencias
scatter(time,var_meta)
hold on
plot(time,calYY)

% Creación del timeStamp
tStamps = datetime('now')-minutes(45):minutes(1):datetime('now');
tStampsF = tStamps';

%% Monoxido
var_mono = mono_s{:,2};

% Calculo de la pendiente
m_mono = time\var_mono;

% Calculo de los valores para Y
calYmono = m_mono*time;
calYYmono = calYmono(:,1)+755;

% Visualización de las tendencias
scatter(time,var_mono)
hold on
plot(time,calYYmono)

%%
% Enviar datos de la tendencia para el Monoxido
thingSpeakWrite(1559284,calYYmono,'WriteKey','TO5W74SMMCQXGHJN','TimeStamp',tStampsF);

% Enviar datos de la tendencia para el Metano
thingSpeakWrite(1574509,calYY,'WriteKey','723A1B0DUSR1IKD5','TimeStamp',tStampsF);

