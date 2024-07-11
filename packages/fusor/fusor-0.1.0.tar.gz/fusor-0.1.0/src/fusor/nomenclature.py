"""Provide helper methods for fusion nomenclature generation."""
from biocommons.seqrepo.seqrepo import SeqRepo
from ga4gh.vrsatile.pydantic.vrs_models import SequenceLocation

from fusor.exceptions import IDTranslationException
from fusor.models import (
    GeneElement,
    RegulatoryClass,
    RegulatoryElement,
    TemplatedSequenceElement,
    TranscriptSegmentElement,
)
from fusor.tools import translate_identifier


def reg_element_nomenclature(element: RegulatoryElement, sr: SeqRepo) -> str:
    """Return fusion nomenclature for regulatory element.
    :param RegulatoryElement element: a regulatory element object
    :param SeqRepo sr: a SeqRepo instance
    :return: regulatory element nomenclature representation
    :raises ValueError: if unable to retrieve genomic location or coordinates,
        or if missing element reference ID, genomic location, and associated
        gene
    """
    element_class = element.regulatory_class.value
    if element_class == RegulatoryClass.ENHANCER:
        type_string = "e"
    elif element_class == RegulatoryClass.PROMOTER:
        type_string = "p"
    else:
        type_string = f"{element.regulatory_class.value}"
    feature_string = ""
    if element.feature_id:
        feature_string += f"_{element.feature_id}"
    elif element.feature_location:
        start = element.feature_location
        sequence_id = start.location.sequence_id
        refseq_id = str(translate_identifier(sr, sequence_id, "refseq")).split(":")[1]
        try:
            chrom = str(translate_identifier(sr, sequence_id, "GRCh38")).split(":")[1]
        except IDTranslationException as e:
            raise ValueError from e
        feature_string += f"_{refseq_id}(chr {chrom}):g.{start.location.interval.start.value}_{start.location.interval.end.value}"
    if element.associated_gene:
        if element.associated_gene.gene_id:
            gene_id = gene_id = element.associated_gene.gene_id

        if element.associated_gene.gene_id:
            gene_id = element.associated_gene.gene_id
        elif element.associated_gene.gene and element.associated_gene.gene.gene_id:
            gene_id = element.associated_gene.gene.gene_id
        else:
            raise ValueError
        feature_string += f"@{element.associated_gene.label}({gene_id})"
    if not feature_string:
        raise ValueError
    return f"reg_{type_string}{feature_string}"


def tx_segment_nomenclature(element: TranscriptSegmentElement) -> str:
    """Return fusion nomenclature for transcript segment element
    :param TranscriptSegmentElement element: a tx segment element. Treated as
    a junction component if only one end is provided.
    :return: element nomenclature representation
    """
    transcript = str(element.transcript)
    if ":" in transcript:
        transcript = transcript.split(":")[1]

    prefix = f"{transcript}({element.gene_descriptor.label})"
    start = element.exon_start if element.exon_start else ""
    if element.exon_start_offset:
        if element.exon_start_offset > 0:
            start_offset = f"+{element.exon_start_offset}"
        else:
            start_offset = str(element.exon_start_offset)
    else:
        start_offset = ""
    end = element.exon_end if element.exon_end else ""
    if element.exon_end_offset:
        if element.exon_end_offset > 0:
            end_offset = f"+{element.exon_end_offset}"
        else:
            end_offset = str(element.exon_end_offset)
    else:
        end_offset = ""
    return f"{prefix}:e.{start}{start_offset}{'_' if start and end else ''}{end}{end_offset}"


def templated_seq_nomenclature(element: TemplatedSequenceElement, sr: SeqRepo) -> str:
    """Return fusion nomenclature for templated sequence element.
    :param TemplatedSequenceElement element: a templated sequence element
    :return: element nomenclature representation
    :raises ValueError: if location isn't a SequenceLocation or if unable
    to retrieve region or location
    """
    if element.region and element.region.location:
        location = element.region.location
        if isinstance(location, SequenceLocation):
            sequence_id = str(location.sequence_id)
            refseq_id = str(translate_identifier(sr, sequence_id, "refseq"))
            start = location.interval.start.value
            end = location.interval.end.value
            try:
                chrom = str(translate_identifier(sr, sequence_id, "GRCh38")).split(":")[
                    1
                ]
            except IDTranslationException as e:
                raise ValueError from e
            return f"{refseq_id.split(':')[1]}(chr {chrom}):g.{start}_{end}({element.strand.value})"
        raise ValueError
    raise ValueError


def gene_nomenclature(element: GeneElement) -> str:
    """Return fusion nomenclature for gene element.
    :param GeneElement element: a gene element object
    :return: element nomenclature representation
    :raises ValueError: if unable to retrieve gene ID
    """
    if element.gene_descriptor.gene_id:
        gene_id = gene_id = element.gene_descriptor.gene_id

    if element.gene_descriptor.gene_id:
        gene_id = element.gene_descriptor.gene_id
    elif element.gene_descriptor.gene and element.gene_descriptor.gene.gene_id:
        gene_id = element.gene_descriptor.gene.gene_id
    else:
        raise ValueError
    return f"{element.gene_descriptor.label}({gene_id})"
