
module pcihellocore (
	pcie_hard_ip_0_rx_in_rx_datain_0,
	pcie_hard_ip_0_tx_out_tx_dataout_0,
	pcie_hard_ip_0_powerdown_pll_powerdown,
	pcie_hard_ip_0_powerdown_gxb_powerdown,
	pcie_hard_ip_0_refclk_export,
	pcie_hard_ip_0_pcie_rstn_export,
	hexdisplay_external_connection_export,
	inport_external_connection_export,
	hexdisplay2_external_connection_export,
	ledgreen_external_connection_export,
	ledred_external_connection_export,
	buttons_external_connection_export);	

	input		pcie_hard_ip_0_rx_in_rx_datain_0;
	output		pcie_hard_ip_0_tx_out_tx_dataout_0;
	input		pcie_hard_ip_0_powerdown_pll_powerdown;
	input		pcie_hard_ip_0_powerdown_gxb_powerdown;
	input		pcie_hard_ip_0_refclk_export;
	input		pcie_hard_ip_0_pcie_rstn_export;
	output	[31:0]	hexdisplay_external_connection_export;
	input	[15:0]	inport_external_connection_export;
	output	[31:0]	hexdisplay2_external_connection_export;
	output	[31:0]	ledgreen_external_connection_export;
	output	[31:0]	ledred_external_connection_export;
	input	[31:0]	buttons_external_connection_export;
endmodule
