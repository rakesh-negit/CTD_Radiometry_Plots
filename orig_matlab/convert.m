% convert uW/cm^2 to umol/(m^2*s)
%
function x = convert(y, lambda)
    hc = 6.626e-34 * 3e8;
    Na = 6.02e23;
    
    % factor of 1e6 to convert uW to W 
    % factor of 100^2 to go from 1/cm^2 to 1/m^2
    x = y .* lambda ./ (1e5 * hc * Na);    
end